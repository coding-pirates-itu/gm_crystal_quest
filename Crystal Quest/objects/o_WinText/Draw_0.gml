// The hero and the crystal, big
draw_sprite_ext(o_Game.sprite_walk, current_time / 150, 540, 230, 6, 6, 0, c_white, 1);
draw_sprite_ext(s_Crystal, current_time / 200, 740, 230, 4, 4, 0, c_white, 1);

draw_set_colour(c_white);
draw_set_halign(fa_center);
draw_set_valign(fa_middle);

draw_set_font(fnt_Win);
draw_set_colour(c_yellow);
draw_text(640, 400, "You win!");

draw_set_font(fnt_Text);
draw_set_colour(c_white);
draw_text(640, 480, "The crystal is back in the village. You reached level " + string(o_Game.level) + ".");
draw_text(640, 560, "Press Enter to play again");
