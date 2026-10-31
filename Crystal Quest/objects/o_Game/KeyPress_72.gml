// H = drink a potion: +2 hearts
if (potions > 0 && hearts < max_hearts && instance_exists(o_Hero))
{
    potions -= 1;
    hearts = min(hearts + 2, max_hearts);
    audio_play_sound(snd_Drink, 1, false);
}
