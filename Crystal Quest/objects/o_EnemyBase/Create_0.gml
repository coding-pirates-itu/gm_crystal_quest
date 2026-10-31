// hp, move_speed, damage, xp and sight are Variable Definitions.
// The children (o_Slime, o_Skeleton, o_Guardian) change them.
walls = layer_tilemap_get_id("Walls");
blockers = [walls, o_LockedDoor, o_RoomExit];   // enemies can't go through these
max_hp = hp;
move_dir = 0;
alarm[0] = 1;

function Hurt(amount)
{
    if (alarm[1] > 0)
    {
        return;      // was just hit
    }

    hp -= amount;
    image_blend = c_red;
    alarm[1] = 15;
    audio_play_sound(snd_Hit, 1, false);

    // Jump back, away from the hero
    var dir = point_direction(o_Hero.x, o_Hero.y, x, y);
    move_and_collide(lengthdir_x(16, dir), lengthdir_y(16, dir), blockers);

    if (hp <= 0)
    {
        o_Game.AddXP(xp);
        instance_create_layer(x, y, "Instances", o_Poof);
        instance_destroy();
    }
}
