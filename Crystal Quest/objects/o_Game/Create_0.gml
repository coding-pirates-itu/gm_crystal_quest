// o_Game is persistent: it lives through all rooms
// and remembers everything about the hero.

// The hero - set on the choose screen, see ChooseHero()
hero_name = "";
max_hearts = 0;
hearts = 0;
damage = 0;
hero_speed = 0;
sprite_idle = s_KnightIdle;
sprite_walk = s_KnightWalk;

// Progress
level = 1;
xp = 0;
xp_next = 5;       // XP needed for the next level
potions = 0;
has_key = false;

// Where o_Hero appears in the next room (-1 = where it is placed in the room editor)
spawn_x = -1;
spawn_y = -1;

// Text at the bottom of the screen, see Say()
message = "";

function ChooseHero(card)
{
    hero_name = card.hero_name;
    max_hearts = card.max_hearts;
    hearts = max_hearts;
    damage = card.damage;
    hero_speed = card.hero_speed;
    sprite_idle = card.sprite_idle;
    sprite_walk = card.sprite_walk;
    room_goto(rm_Village);
}

// Show a message for 3 seconds
function Say(text)
{
    message = text;
    alarm[1] = 3 * game_get_speed(gamespeed_fps);
}

function AddXP(amount)
{
    xp += amount;
    if (xp >= xp_next)
    {
        level += 1;
        xp_next += 5;
        max_hearts += 1;
        hearts = max_hearts;
        damage += 1;
        audio_play_sound(snd_LevelUp, 1, false);
        Say("Level up! You are now level " + string(level) + ".");
    }
}

function Faint()
{
    audio_play_sound(snd_Faint, 1, false);
    Say("You fainted... and woke up in the village.");
    alarm[0] = 2 * game_get_speed(gamespeed_fps);
}
