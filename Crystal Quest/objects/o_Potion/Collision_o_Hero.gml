o_Game.potions += 1;
o_Game.Say("You found a potion. Press H to drink it.");
audio_play_sound(snd_Pickup, 1, false);
instance_destroy();
