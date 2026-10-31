if (image_index == 0)
{
    image_index = 1;
    o_Game.has_key = true;
    o_Game.Say("You found the key to the dungeon!");
    audio_play_sound(snd_Pickup, 1, false);
}
