// Generates the game's sound effects with jsfxr (sfxr, https://sfxr.me, public domain).
const fs = require("fs");
const { sfxr } = require("jsfxr");
const out = process.argv[2];

const base = {
  oldParams: true, wave_type: 0,
  p_env_attack: 0, p_env_sustain: 0.3, p_env_punch: 0, p_env_decay: 0.4,
  p_base_freq: 0.3, p_freq_limit: 0, p_freq_ramp: 0, p_freq_dramp: 0,
  p_vib_strength: 0, p_vib_speed: 0, p_arp_mod: 0, p_arp_speed: 0,
  p_duty: 0, p_duty_ramp: 0, p_repeat_speed: 0, p_pha_offset: 0, p_pha_ramp: 0,
  p_lpf_freq: 1, p_lpf_ramp: 0, p_lpf_resonance: 0, p_hpf_freq: 0, p_hpf_ramp: 0,
  sound_vol: 0.5, sample_rate: 44100, sample_size: 16,
};
// wave_type: 0 square, 1 sawtooth, 2 sine, 3 noise
const sounds = {
  // sword swing
  snd_Swing: { wave_type: 3, p_env_sustain: 0.06, p_env_decay: 0.18, p_base_freq: 0.7, p_freq_ramp: -0.3, p_hpf_freq: 0.35, sound_vol: 0.25 },
  // sword hits an enemy
  snd_Hit: { wave_type: 3, p_env_sustain: 0.05, p_env_punch: 0.5, p_env_decay: 0.2, p_base_freq: 0.35, p_freq_ramp: -0.2, sound_vol: 0.25 },
  // the hero is hurt
  snd_Hurt: { wave_type: 0, p_env_sustain: 0.1, p_env_punch: 0.3, p_env_decay: 0.25, p_base_freq: 0.45, p_freq_ramp: -0.35, p_duty: 0.2, sound_vol: 0.3 },
  // potion or key picked up
  snd_Pickup: { wave_type: 1, p_env_sustain: 0.05, p_env_punch: 0.45, p_env_decay: 0.3, p_base_freq: 0.6, p_arp_speed: 0.6, p_arp_mod: 0.45, sound_vol: 0.25 },
  // drinking a potion
  snd_Drink: { wave_type: 2, p_env_sustain: 0.25, p_env_decay: 0.2, p_base_freq: 0.3, p_freq_ramp: 0.15, p_vib_strength: 0.5, p_vib_speed: 0.6, sound_vol: 0.4 },
  // level up
  snd_LevelUp: { wave_type: 0, p_env_sustain: 0.3, p_env_decay: 0.35, p_base_freq: 0.3, p_freq_ramp: 0.25, p_duty: 0.4, p_repeat_speed: 0.55, sound_vol: 0.3 },
  // the locked door opens
  snd_Door: { wave_type: 1, p_env_sustain: 0.25, p_env_decay: 0.25, p_base_freq: 0.12, p_freq_ramp: 0.05, p_vib_strength: 0.4, p_vib_speed: 0.7, p_lpf_freq: 0.5, sound_vol: 0.3 },
  // the villager heals
  snd_Heal: { wave_type: 2, p_env_sustain: 0.3, p_env_decay: 0.3, p_base_freq: 0.45, p_arp_speed: 0.55, p_arp_mod: -0.3, sound_vol: 0.35 },
  // the hero faints
  snd_Faint: { wave_type: 0, p_env_sustain: 0.4, p_env_decay: 0.45, p_base_freq: 0.4, p_freq_ramp: -0.15, p_duty: 0.5, p_vib_strength: 0.2, p_vib_speed: 0.4, sound_vol: 0.3 },
  // the crystal is found
  snd_Win: { wave_type: 0, p_env_sustain: 0.35, p_env_punch: 0.3, p_env_decay: 0.45, p_base_freq: 0.4, p_arp_speed: 0.65, p_arp_mod: -0.35, p_duty: 0.3, p_repeat_speed: 0.4, sound_vol: 0.3 },
};

for (const [name, def] of Object.entries(sounds)) {
  const wave = sfxr.toWave(Object.assign({}, base, def));
  fs.writeFileSync(`${out}/${name}.wav`, Buffer.from(wave.wav));
  console.log(name, ((wave.wav.length - 44) / 2 / 44100).toFixed(3));
}
