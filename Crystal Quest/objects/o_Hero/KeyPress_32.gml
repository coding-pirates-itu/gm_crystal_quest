// Space = swing the sword, one swing at a time
if (instance_exists(o_Sword))
{
    exit;
}

var sword = instance_create_layer(x + lengthdir_x(20, facing), y + lengthdir_y(20, facing), "Instances", o_Sword);
sword.image_angle = facing;
audio_play_sound(snd_Swing, 1, false);
