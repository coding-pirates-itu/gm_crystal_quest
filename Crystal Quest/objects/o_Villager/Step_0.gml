// Talk and heal when the hero stands close.
// say is a Variable Definition, set in the room editor.
if (instance_exists(o_Hero) && point_distance(x, y, o_Hero.x, o_Hero.y) < 48)
{
    o_Game.Say(say);
    if (o_Game.hearts < o_Game.max_hearts)
    {
        o_Game.hearts = o_Game.max_hearts;
        audio_play_sound(snd_Heal, 1, false);
    }
}
