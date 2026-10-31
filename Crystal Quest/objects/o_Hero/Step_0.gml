// Walk with the arrow keys
var dx = keyboard_check(vk_right) - keyboard_check(vk_left);
var dy = keyboard_check(vk_down) - keyboard_check(vk_up);

if (dx != 0 || dy != 0)
{
    facing = point_direction(0, 0, dx, dy);
    move_and_collide(dx * o_Game.hero_speed, dy * o_Game.hero_speed, walls);
    sprite_index = sprite_walk;
    if (dx != 0)
    {
        image_xscale = dx;     // look left or right
    }
}
else
{
    sprite_index = sprite_idle;
}

// See-through while invincible
if (alarm[0] > 0)
{
    image_alpha = 0.5;
}
else
{
    image_alpha = 1;
}
