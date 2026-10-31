draw_self();

// Health bar above the guardian
draw_healthbar(x - 32, y - 44, x + 32, y - 38, hp / max_hp * 100, c_black, c_red, c_lime, 0, true, true);
