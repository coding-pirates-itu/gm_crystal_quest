// Chase the hero when it is close, otherwise wander around
if (instance_exists(o_Hero) && point_distance(x, y, o_Hero.x, o_Hero.y) < sight)
{
    move_dir = point_direction(x, y, o_Hero.x, o_Hero.y);
}

move_and_collide(lengthdir_x(move_speed, move_dir), lengthdir_y(move_speed, move_dir), blockers);
