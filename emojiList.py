
import discord
import emojiSecs



face = ":grinning: :grimacing: :grin: :joy: :smiley: :smile: :sweat_smile: :laughing: :innocent: :wink: :blush: :slight_smile: :upside_down: :relaxed: :yum: :relieved: :heart_eyes: :kissing_heart: :kissing: :kissing_smiling_eyes: :kissing_closed_eyes: :stuck_out_tongue_winking_eye: :stuck_out_tongue_closed_eyes: :stuck_out_tongue: :money_mouth: :nerd: :sunglasses: :hugging: :smirk: :no_mouth: :neutral_face: :expressionless: :unamused: :rolling_eyes: :thinking: :flushed: :disappointed: :worried: :angry: :rage: :pensive: :confused: :slight_frown: :frowning2: :persevere: :confounded: :tired_face: :weary: :triumph: :open_mouth: :scream: :fearful: :cold_sweat: :hushed: :frowning: :anguished: :cry: :disappointed_relieved: :sleepy: :sweat: :sob: :dizzy_face: :astonished: :zipper_mouth: :mask: :thermometer_face: :head_bandage: :sleeping: :smiling_imp: :imp: :smiley_cat: :smile_cat: :joy_cat: :heart_eyes_cat: :smirk_cat: :kissing_cat: :scream_cat: :crying_cat_face: :pouting_cat:".split()

person = ":baby: :boy: :girl: :man: :woman: :person_with_blond_hair: :older_man: :older_woman: :man_with_gua_pi_mao: :man_with_turban: :cop: :construction_worker: :guardsman: :spy: :santa: :angel: :princess: :bride_with_veil: :dancer: :prince: :man_in_tuxedo: :mrs_claus: :juggling: :basketball_player: :surfer: :levitate: :mountain_bicyclist: :horse_racing: :golfer:".split()

hand = ":raised_hands: :clap: :wave: :thumbsup: :thumbsdown: :punch: :fist: :v: :ok_hand: :raised_hand: :open_hands: :muscle: :pray: :point_up: :point_up_2: :point_down: :point_left: :point_right: :middle_finger: :hand_splayed: :metal: :vulcan: :writing_hand: :call_me: :raised_back_of_hand: :left_facing_fist: :right_facing_fist: :handshake: :fingers_crossed: ".split()

letter = ":regional_indicator_a: :regional_indicator_b: :regional_indicator_c: :regional_indicator_d: :regional_indicator_e: :regional_indicator_f: :regional_indicator_g: :regional_indicator_h: :regional_indicator_i: :regional_indicator_j: :regional_indicator_k: :regional_indicator_l: :regional_indicator_m: :regional_indicator_n: :regional_indicator_o: :regional_indicator_p: :regional_indicator_q: :regional_indicator_r: :regional_indicator_s: :regional_indicator_t: :regional_indicator_u: :regional_indicator_v: :regional_indicator_w: :regional_indicator_x: :regional_indicator_y: :regional_indicator_z: ".split()

flag = ":flag_ac: :flag_af: :flag_al: :flag_dz: :flag_ad: :flag_ao: :flag_ai: :flag_ag: :flag_ar: :flag_am: :flag_aw: :flag_au: :flag_at: :flag_az: :flag_bs: :flag_bh: :flag_bd: :flag_bb: :flag_by: :flag_be: :flag_bz: :flag_bj: :flag_bm: :flag_bt: :flag_bo: :flag_ba: :flag_bw: :flag_br: :flag_bn: :flag_bg: :flag_bf: :flag_bi: :flag_cv: :flag_kh: :flag_cm: :flag_ca: :flag_ky: :flag_cf: :flag_td: :flag_cl: :flag_cn: :flag_co: :flag_km: :flag_cg: :flag_cd: :flag_cr: :flag_hr: :flag_cu: :flag_cy: :flag_cz: :flag_dk: :flag_dj: :flag_dm: :flag_do: :flag_ec: :flag_eg: :flag_sv: :flag_gq: :flag_er: :flag_ee: :flag_et: :flag_fk: :flag_fo: :flag_fj: :flag_fi: :flag_fr: :flag_pf: :flag_ga: :flag_gm: :flag_ge: :flag_de: :flag_gh: :flag_gi: :flag_gr: :flag_gl: :flag_gd: :flag_gu: :flag_gt: :flag_gn: :flag_gw: :flag_gy: :flag_ht: :flag_hn: :flag_hk: :flag_hu: :flag_is: :flag_in: :flag_id: :flag_ir: :flag_iq: :flag_ie: :flag_il: :flag_it: :flag_ci: :flag_jm: :flag_jp: :flag_je: :flag_jo: :flag_kz: :flag_ke: :flag_ki: :flag_xk: :flag_kw: :flag_kg: :flag_la: :flag_lv: :flag_lb: :flag_ls: :flag_lr: :flag_ly: :flag_li: :flag_lt: :flag_lu: :flag_mo: :flag_mk: :flag_mg: :flag_mw: :flag_my: :flag_mv: :flag_ml: :flag_mt: :flag_mh: :flag_mr: :flag_mu: :flag_mx: :flag_fm: :flag_md: :flag_mc: :flag_mn: :flag_me: :flag_ma: :flag_ms: :flag_mz: :flag_mm: :flag_na: :flag_nr: :flag_np: :flag_nl: :flag_nc: :flag_nz: :flag_ni: :flag_ne: :flag_ng: :flag_nu: :flag_kp: :flag_no: :flag_om: :flag_pk: :flag_pw: :flag_ps: :flag_pa: :flag_pg: :flag_py: :flag_pe: :flag_ph: :flag_pl: :flag_pt: :flag_pr: :flag_qa: :flag_ro: :flag_ru: :flag_rw: :flag_sh: :flag_kn: :flag_lc: :flag_vc: :flag_ws: :flag_sm: :flag_st: :flag_sa: :flag_sn: :flag_rs: :flag_sc: :flag_sl: :flag_sg: :flag_sk: :flag_si: :flag_sb: :flag_so: :flag_za: :flag_kr: :flag_es: :flag_lk: :flag_sd: :flag_sr: :flag_sz: :flag_se: :flag_ch: :flag_sy: :flag_tw: :flag_tj: :flag_tz: :flag_th: :flag_tl: :flag_tg: :flag_to: :flag_tt: :flag_tn: :flag_tr: :flag_tm: :flag_tv: :flag_ug: :flag_ua: :flag_ae: :flag_gb: :flag_us: :flag_vi: :flag_uy: :flag_uz: :flag_vu: :flag_va: :flag_ve: :flag_vn: :flag_wf: :flag_eh: :flag_ye: :flag_zm: :flag_zw: :flag_re: :flag_ax: :flag_ta: :flag_io: :flag_bq: :flag_cx: :flag_cc: :flag_gg: :flag_im: :flag_yt: :flag_nf: :flag_pn: :flag_ea: :flag_ic: :flag_um: :flag_sj: :flag_hm: :flag_bv: :flag_tk: :flag_gs: :flag_pm: :flag_bl: :flag_cp: :flag_dg: :flag_as: :flag_aq: :flag_vg: :flag_ck: :flag_cw: :flag_eu: :flag_gf: :flag_tf: :gay_pride_flag: :flag_mf: :flag_tc: :flag_ss: :flag_sx: :flag_mp: :flag_mq: :flag_gp: ".split()

animal = ":dog: :cat: :mouse: :rabbit: :hamster: :bear: :panda_face: :koala: :tiger: :lion_face: :cow: :pig: :frog: :octopus: :monkey_face: :see_no_evil: :hear_no_evil: :speak_no_evil: :monkey: :chicken: :penguin: :bird: :baby_chick: :hatching_chick: :hatched_chick: :wolf: :boar: :horse: :unicorn: :bee: :bug: :snail: :beetle: :ant: :spider: :scorpion: :crab: :snake: :turtle: :tropical_fish: :fish: :blowfish: :dolphin: :whale: :crocodile: :whale2: :leopard: :tiger2: :water_buffalo: :ox: :cow2: :dromedary_camel: :camel: :elephant: :goat: :ram: :sheep: :racehorse: :pig2: :rat: :mouse2: :rooster: :turkey: :dove: :dog2: :poodle: :cat2: :rabbit2: :chipmunk: :dragon: :dragon_face: :eagle: :duck: :bat: :shark: :owl: :fox: :butterfly: :deer: :gorilla: :lizard: :rhino: :shrimp: :squid: ".split()

food = ":green_apple: :apple: :pear: :tangerine: :lemon: :banana: :watermelon: :grapes: :strawberry: :melon: :bread: :honey_pot: :sweet_potato: :corn: :hot_pepper: :eggplant: :tomato: :pineapple: :peach: :cherries: :cheese: :poultry_leg: :meat_on_bone: :fried_shrimp: :cooking: :hamburger: :fries: :hotdog: :pizza: :spaghetti: :rice: :rice_ball: :curry: :bento: :sushi: :fish_cake: :stew: :ramen: :burrito: :taco: :rice_cracker: :oden: :dango: :shaved_ice: :ice_cream: :icecream: :cake: :birthday: :custard: :candy: :tropical_drink: :cocktail: :wine_glass: :beers: :beer: :cookie: :doughnut: :popcorn: :chocolate_bar: :lollipop: :champagne: :sake: :tea: :coffee: :baby_bottle: :croissant: :avocado: :cucumber: :bacon: :potato: :carrot: :french_bread: :salad: :shallow_pan_of_food: :stuffed_flatbread: :champagne_glass: :tumbler_glass: :pancakes: :kiwi: :peanuts: :egg: ".split()

car = ":red_car: :taxi: :blue_car: :bus: :trolleybus: :race_car: :police_car: :ambulance: :fire_engine: :minibus: :truck: :articulated_lorry: :tractor: :motorcycle: :bike: :oncoming_police_car: :oncoming_bus: :oncoming_automobile: :oncoming_taxi: ".split()

place = ":ferris_wheel: :roller_coaster: :carousel_horse: :construction_site: :foggy: :tokyo_tower: :fountain: :rice_scene: :mountain: :mountain_snow: :mount_fuji: :volcano: :japan: :camping: :tent: :park: :motorway: :railway_track: :sunrise: :sunrise_over_mountains: :desert: :beach: :island: :city_sunset: :city_dusk: :cityscape: :night_with_stars: :bridge_at_night: :milky_way: :stars: :sparkler: :fireworks: :rainbow: :homes: :statue_of_liberty: :stadium: ".split()

plant = ":cactus: :christmas_tree: :evergreen_tree: :deciduous_tree: :palm_tree: :seedling: :herb: :sunflower: :hibiscus: :ear_of_rice: :maple_leaf: :fallen_leaf: :leaves: :tanabata_tree: :bamboo: :four_leaf_clover: :shamrock: :rose: :tulip: :blossom: :cherry_blossom: :bouquet: :mushroom: :chestnut: :jack_o_lantern: :wilted_rose: ".split()

weather = ":sunny: :white_sun_small_cloud: :partly_sunny: :white_sun_cloud: :white_sun_rain_cloud: :cloud: :cloud_rain: :thunder_cloud_rain: :cloud_lightning: :zap: :snowflake: :cloud_snow: :wind_blowing_face: :cloud_tornado: :droplet:".split()

couple = ":couple: :wrestlers: :two_men_holding_hands: :two_women_holding_hands: :couple_with_heart: :couple_ww: :couple_mm: :couplekiss: :kiss_ww: :kiss_mm:".split()

family = ":family: :family_mwg: :family_mwgb: :family_mwbb: :family_mwgg: :family_wwb: :family_wwg: :family_wwgb: :family_wwbb: :family_wwgg: :family_mmb: :family_mmg: :family_mmgb: :family_mmbb: :family_mmgg:".split()

moonPhases = {0 : ":full_moon:", 1 : ":waning_gibbous_moon:", 2 : ":last_quarter_moon:", 3 : ":waning_crescent_moon:", 4 : ":new_moon:", 5 : ":waxing_crescent_moon:", 6 : ":first_quarter_moon:", 7 : ":waxing_gibbous_moon:"}

def getMembers(msg):
    a = []
    n = msg.server
    for i in n.members:
        a += [i]
    print("Getting Members from msg \n {}...\n in server {}...").format(msg.content,n.name)
    return a

message = ''






"https://discord.gg/Gtge2hD"


helpMe = ["""```!random face
!random person
!random family
!random couple
!random hand
!random letter
!random flag
!random animal
!random food
!random car
!random place
!random plant
!random weather
!random emoji

!random user
!random online```"""]


randEmojis = {"smash" : emojiSecs.smash4, "meme" : [],"emoji" : emojiSecs.sAll, "family" : family, "couple" : couple,"plant" : plant, "weather" : weather,"help" : helpMe, "car" : car, 'face' : face, 'person' : person, 'place' : place, 'hand' : hand, "letter" : letter, "flag" : flag, "animal" : animal, "food" : food}

combo69 = {1 : "nice",
2 : "niice",
3 : "dude, nice",
4 : "dude, NICE",
5 : "NIIICE",
6 : "DUDE. NIICE.",
}

def counter69(count):
    what = 'II'
    huh = ''
    eh = ''
    for i in range(count-6):
        what += 'I'
        if i % 2 == 0:
            huh += 'O'
        if i % 3 == 0:
            eh += 'U'
    return "W"+ huh +"W. D"+eh+"DE. N" + what + "CE."
