draw_set_colour(c_white);
draw_set_valign(fa_top);

if (room == rm_Choose)
{
    draw_set_font(fnt_Win);
    draw_set_halign(fa_center);
    draw_text(640, 40, "Choose your hero");
    exit;
}

if (room == rm_Win)
{
    exit;
}

// Hearts
for (var i = 0; i < max_hearts; i++)
{
    var frame = 0;          // full heart
    if (i >= hearts)
    {
        frame = 1;          // empty heart
    }
    draw_sprite_ext(s_Heart, frame, 16 + i * 36, 16, 2, 2, 0, c_white, 1);
}

// Potions and the key
draw_sprite_ext(s_Potion, 0, 36, 80, 1.5, 1.5, 0, c_white, 1);
draw_set_font(fnt_Text);
draw_set_halign(fa_left);
draw_text(60, 58, "x " + string(potions));
if (has_key)
{
    draw_sprite_ext(s_Key, 0, 120, 60, 2.5, 2.5, 0, c_white, 1);
}

// Level and XP
draw_set_font(fnt_Hud);
draw_set_halign(fa_right);
draw_text(1264, 8, hero_name + "  Level " + string(level) + "  XP " + string(xp) + " / " + string(xp_next));

// Message box
if (message != "")
{
    draw_set_alpha(0.7);
    draw_set_colour(c_black);
    draw_rectangle(40, 560, 1240, 680, false);
    draw_set_alpha(1);
    draw_set_colour(c_white);
    draw_set_font(fnt_Text);
    draw_set_halign(fa_left);
    draw_text_ext(64, 572, message, 44, 1150);
}
