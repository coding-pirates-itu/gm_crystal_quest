// hero_name, max_hearts, damage, hero_speed, sprite_idle and sprite_walk
// are Variable Definitions, set for each card in the room editor.
draw_self();

// The hero, walking, 5 times bigger
draw_sprite_ext(sprite_walk, current_time / 150, x + 128, y + 110, 5, 5, 0, c_white, 1);

draw_set_colour(c_black);
draw_set_halign(fa_center);
draw_set_valign(fa_top);
draw_set_font(fnt_Hud);
draw_text(x + 128, y + 210, hero_name);

draw_set_font(fnt_Text);
draw_text(x + 128, y + 280, "Hearts: " + string(max_hearts));
draw_text(x + 128, y + 325, "Damage: " + string(damage));
draw_text(x + 128, y + 370, "Speed: " + string(hero_speed));
