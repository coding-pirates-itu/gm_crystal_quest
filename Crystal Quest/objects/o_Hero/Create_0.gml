walls = layer_tilemap_get_id("Walls");   // everything painted on this layer blocks
facing = 0;      // for the sword: 0 = right, 90 = up, 180 = left, 270 = down

sprite_idle = o_Game.sprite_idle;
sprite_walk = o_Game.sprite_walk;
sprite_index = sprite_idle;

// Came through a room exit? Then appear where the exit says.
if (o_Game.spawn_x >= 0)
{
    x = o_Game.spawn_x;
    y = o_Game.spawn_y;
}

function Hurt(amount, enemy)
{
    if (alarm[0] > 0)
    {
        return;      // still invincible
    }

    o_Game.hearts -= amount;
    audio_play_sound(snd_Hurt, 1, false);

    // Jump back, away from the enemy
    var dir = point_direction(enemy.x, enemy.y, x, y);
    move_and_collide(lengthdir_x(24, dir), lengthdir_y(24, dir), walls);

    // Invincible for 1 second
    alarm[0] = game_get_speed(gamespeed_fps);

    if (o_Game.hearts <= 0)
    {
        instance_create_layer(x, y, "Instances", o_Poof);
        o_Game.Faint();
        instance_destroy();
    }
}
