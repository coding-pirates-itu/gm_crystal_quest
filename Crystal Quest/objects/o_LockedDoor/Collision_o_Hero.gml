if (o_Game.has_key)
{
    audio_play_sound(snd_Door, 1, false);
    instance_destroy();
}
else
{
    o_Game.Say("The door is locked. The key must be somewhere in the forest.");

    // Push the hero back to where it was
    other.x = other.xprevious;
    other.y = other.yprevious;
}
