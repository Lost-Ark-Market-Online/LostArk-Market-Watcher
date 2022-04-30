from difflib import get_close_matches


market_map = {
    'Fresh Mushroom': {
        'name': 'Fresh Mushroom',
        'amount': 10,
        'image': 'fresh_mushroom.webp',
        'category': 'Trader',
        'subcategory': 'Foraging Rewards',
        'rarity': 1
    },
    'Shy Wild Flower': {
        'name': 'Shy Wild Flower',
        'amount': 10,
        'image': 'shy_wild_flower.webp',
        'category': 'Trader',
        'subcategory': 'Foraging Rewards',
        'rarity': 1
    },
    'Exquisite Mushroom': {
        'name': 'Exquisite Mushroom',
        'amount': 10,
        'image': 'exquisite_mushroom.webp',
        'category': 'Trader',
        'subcategory': 'Foraging Rewards',
        'rarity': 2
    },
    'Bright Wild Flower': {
        'name': 'Bright Wild Flower',
        'amount': 10,
        'image': 'bright_wild_flower.webp',
        'category': 'Trader',
        'subcategory': 'Foraging Rewards',
        'rarity': 2
    },
    'Crude Mushroom': {
        'name': 'Crude Mushroom',
        'amount': 100,
        'image': 'crude_mushroom.webp',
        'category': 'Trader',
        'subcategory': 'Foraging Rewards',
        'rarity': 0
    },
    'Wild Flower': {
        'name': 'Wild Flower',
        'amount': 100,
        'image': 'wild_flower.webp',
        'category': 'Trader',
        'subcategory': 'Foraging Rewards',
        'rarity': 0
    },
    'Tender Timber': {
        'name': 'Tender Timber',
        'amount': 10,
        'image': 'tender_timber.webp',
        'category': 'Trader',
        'subcategory': 'Logging Loot',
        'rarity': 1
    },
    'Sturdy Timber': {
        'name': 'Sturdy Timber',
        'amount': 10,
        'image': 'sturdy_timber.webp',
        'category': 'Trader',
        'subcategory': 'Logging Loot',
        'rarity': 2
    },
    'Timber': {
        'name': 'Timber',
        'amount': 100,
        'image': 'timber.webp',
        'category': 'Trader',
        'subcategory': 'Logging Loot',
        'rarity': 0
    },
    'Heavy Iron Ore': {
        'name': 'Heavy Iron Ore',
        'amount': 10,
        'image': 'heavy_iron_ore.webp',
        'category': 'Trader',
        'subcategory': 'Mining Loot',
        'rarity': 1
    },
    'Strong Iron Ore': {
        'name': 'Strong Iron Ore',
        'amount': 10,
        'image': 'strong_iron_ore.webp',
        'category': 'Trader',
        'subcategory': 'Mining Loot',
        'rarity': 2
    },
    'Iron Ore': {
        'name': 'Iron Ore',
        'amount': 100,
        'image': 'iron_ore.webp',
        'category': 'Trader',
        'subcategory': 'Mining Loot',
        'rarity': 0
    },
    'Treated Meat': {
        'name': 'Treated Meat',
        'amount': 10,
        'image': 'treated_meat.webp',
        'category': 'Trader',
        'subcategory': 'Hunting Loot',
        'rarity': 1
    },
    'Tough Leather': {
        'name': 'Tough Leather',
        'amount': 10,
        'image': 'tough_leather.webp',
        'category': 'Trader',
        'subcategory': 'Hunting Loot',
        'rarity': 1
    },
    'Caldarr Thick Raw Meat': {
        'name': 'Caldarr Thick Raw Meat',
        'amount': 10,
        'image': 'caldarr_thick_raw_meat.webp',
        'category': 'Trader',
        'subcategory': 'Hunting Loot',
        'rarity': 2
    },
    'Oreha Thick Meat': {
        'name': 'Oreha Thick Meat',
        'amount': 10,
        'image': 'oreha_thick_meat.webp',
        'category': 'Trader',
        'subcategory': 'Hunting Loot',
        'rarity': 2
    },
    'Thick Raw Meat': {
        'name': 'Thick Raw Meat',
        'amount': 100,
        'image': 'thick_raw_meat.webp',
        'category': 'Trader',
        'subcategory': 'Hunting Loot',
        'rarity': 0
    },
    'Hunting Crystal': {
        'name': 'Hunting Crystal',
        'amount': 10,
        'image': 'hunting_crystal.webp',
        'category': 'Trader',
        'subcategory': 'Hunting Loot',
        'rarity': 3
    },
    'Natural Pearl': {
        'name': 'Natural Pearl',
        'amount': 10,
        'image': 'natural_pearl.webp',
        'category': 'Trader',
        'subcategory': 'Fishing Loot',
        'rarity': 1
    },
    'Redflesh Fish': {
        'name': 'Redflesh Fish',
        'amount': 10,
        'image': 'redflesh_fish.webp',
        'category': 'Trader',
        'subcategory': 'Fishing Loot',
        'rarity': 1
    },
    'Caldarr Solar Carp': {
        'name': 'Caldarr Solar Carp',
        'amount': 10,
        'image': 'caldarr_solar_carp.webp',
        'category': 'Trader',
        'subcategory': 'Fishing Loot',
        'rarity': 2
    },
    'Oreha Solar Carp': {
        'name': 'Oreha Solar Carp',
        'amount': 10,
        'image': 'oreha_solar_carp.webp',
        'category': 'Trader',
        'subcategory': 'Fishing Loot',
        'rarity': 2
    },
    'Fish': {
        'name': 'Fish',
        'amount': 100,
        'image': 'fish.webp',
        'category': 'Trader',
        'subcategory': 'Fishing Loot',
        'rarity': 0
    },
    'Fishing Crystal': {
        'name': 'Fishing Crystal',
        'amount': 10,
        'image': 'fishing_crystal.webp',
        'category': 'Trader',
        'subcategory': 'Fishing Loot',
        'rarity': 3
    },
    'Oreha Relic': {
        'name': 'Oreha Relic',
        'amount': 10,
        'image': 'oreha_relic.webp',
        'category': 'Trader',
        'subcategory': 'Excavating Loot',
        'rarity': 2
    },
    'Caldarr Relic': {
        'name': 'Caldarr Relic',
        'amount': 10,
        'image': 'caldarr_relic.webp',
        'category': 'Trader',
        'subcategory': 'Excavating Loot',
        'rarity': 2
    },
    'Rare Relic': {
        'name': 'Rare Relic',
        'amount': 10,
        'image': 'rare_relic.webp',
        'category': 'Trader',
        'subcategory': 'Excavating Loot',
        'rarity': 1
    },
    'Excavating Crystal': {
        'name': 'Excavating Crystal',
        'amount': 10,
        'image': 'excavating_crystal.webp',
        'category': 'Trader',
        'subcategory': 'Excavating Loot',
        'rarity': 3
    },
    'Ancient Relic': {
        'name': 'Ancient Relic',
        'amount': 100,
        'image': 'ancient_relic.webp',
        'category': 'Trader',
        'subcategory': 'Excavating Loot',
        'rarity': 0
    },
    'Apprentice Craft Kit': {
        'name': 'Apprentice Craft Kit',
        'amount': 1,
        'image': 'apprentice_craft_kit.webp',
        'category': 'Trader',
        'subcategory': 'Other',
        'rarity': 2
    },
    'Adept Craft Kit': {
        'name': 'Adept Craft Kit',
        'amount': 1,
        'image': 'adept_craft_kit.webp',
        'category': 'Trader',
        'subcategory': 'Other',
        'rarity': 3
    },
    'Tool Crafting Part': {
        'name': 'Tool Crafting Part',
        'amount': 1,
        'image': 'tool_crafting_part.webp',
        'category': 'Trader',
        'subcategory': 'Other',
        'rarity': 1
    },
    'Expert Craft Kit': {
        'name': 'Expert Craft Kit',
        'amount': 1,
        'image': 'expert_craft_kit.webp',
        'category': 'Trader',
        'subcategory': 'Other',
        'rarity': 4
    },
    'Master Craft Kit': {
        'name': 'Master Craft Kit',
        'amount': 1,
        'image': 'master_craft_kit.webp',
        'category': 'Trader',
        'subcategory': 'Other',
        'rarity': 5
    },
    'Destruction Stone Fragment': {
        'name': 'Destruction Stone Fragment',
        'amount': 10,
        'image': 'destruction_stone_fragment.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 0
    },
    'Guardian Stone Fragment': {
        'name': 'Guardian Stone Fragment',
        'amount': 10,
        'image': 'guardian_stone_fragment.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 0
    },
    'Guardian Stone': {
        'name': 'Guardian Stone',
        'amount': 10,
        'image': 'guardian_stone.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 0
    },
    'Destruction Stone': {
        'name': 'Destruction Stone',
        'amount': 10,
        'image': 'destruction_stone.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 0
    },
    'Guardian Stone Crystal': {
        'name': 'Guardian Stone Crystal',
        'amount': 10,
        'image': 'guardian_stone_crystal.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 0
    },
    'Destruction Stone Crystal': {
        'name': 'Destruction Stone Crystal',
        'amount': 10,
        'image': 'destruction_stone_crystal.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 0
    },
    'Simple Oreha Fusion Material': {
        'name': 'Simple Oreha Fusion Material',
        'amount': 1,
        'image': 'simple_oreha_fusion_material.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 1
    },
    'Harmony Shard Pouch (S)': {
        'name': 'Harmony Shard Pouch (S)',
        'amount': 1,
        'image': 'harmony_shard_pouch_s.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 1
    },
    'Life Shard Pouch (S)': {
        'name': 'Life Shard Pouch (S)',
        'amount': 1,
        'image': 'life_shard_pouch_s.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 1
    },
    'Honor Shard Pouch (S)': {
        'name': 'Honor Shard Pouch (S)',
        'amount': 1,
        'image': 'honor_shard_pouch_s.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 1
    },
    'Caldarr Fusion Material': {
        'name': 'Caldarr Fusion Material',
        'amount': 1,
        'image': 'caldarr_fusion_material.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 2
    },
    'Basic Oreha Fusion Material': {
        'name': 'Basic Oreha Fusion Material',
        'amount': 1,
        'image': 'basic_oreha_fusion_material.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 2
    },
    'Harmony Shard Pouch (M)': {
        'name': 'Harmony Shard Pouch (M)',
        'amount': 1,
        'image': 'harmony_shard_pouch_m.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 2
    },
    'Life Shard Pouch (M)': {
        'name': 'Life Shard Pouch (M)',
        'amount': 1,
        'image': 'life_shard_pouch_m.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 2
    },
    'Honor Shard Pouch (M)': {
        'name': 'Honor Shard Pouch (M)',
        'amount': 1,
        'image': 'honor_shard_pouch_m.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 2
    },
    'Harmony Shard Pouch (L)': {
        'name': 'Harmony Shard Pouch (L)',
        'amount': 1,
        'image': 'harmony_shard_pouch_l.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 3
    },
    'Life Shard Pouch (L)': {
        'name': 'Life Shard Pouch (L)',
        'amount': 1,
        'image': 'life_shard_pouch_l.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 3
    },
    'Honor Shard Pouch (L)': {
        'name': 'Honor Shard Pouch (L)',
        'amount': 1,
        'image': 'honor_shard_pouch_l.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Honing Materials',
        'rarity': 3
    },
    'Solar Grace': {
        'name': 'Solar Grace',
        'amount': 1,
        'image': 'solar_grace.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 1
    },
    'Harmony Leapstone': {
        'name': 'Harmony Leapstone',
        'amount': 1,
        'image': 'harmony_leapstone.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 2
    },
    'Life Leapstone': {
        'name': 'Life Leapstone',
        'amount': 1,
        'image': 'life_leapstone.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 2
    },
    'Honor Leapstone': {
        'name': 'Honor Leapstone',
        'amount': 1,
        'image': 'honor_leapstone.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 2
    },
    'Great Honor Leapstone': {
        'name': 'Great Honor Leapstone',
        'amount': 1,
        'image': 'great_honor_leapstone.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 2
    },
    'Solar Blessing': {
        'name': 'Solar Blessing',
        'amount': 1,
        'image': 'solar_blessing.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 2
    },
    'Star\'s Breath': {
        'name': 'Star\'s Breath',
        'amount': 1,
        'image': 'stars_breath.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Tailoring: Basic Design': {
        'name': 'Tailoring: Basic Design',
        'amount': 1,
        'image': 'tailoring_basic_design.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Metallurgy Basic Casting': {
        'name': 'Metallurgy Basic Casting',
        'amount': 1,
        'image': 'metallurgy_basic_casting.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Moon\'s Breath': {
        'name': 'Moon\'s Breath',
        'amount': 1,
        'image': 'moons_breath.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Tailoring: Basic Knots': {
        'name': 'Tailoring: Basic Knots',
        'amount': 1,
        'image': 'tailoring_basic_knots.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Metallurgy: Basic Folding': {
        'name': 'Metallurgy: Basic Folding',
        'amount': 1,
        'image': 'metallurgy_basic_folding.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Solar Protection': {
        'name': 'Solar Protection',
        'amount': 1,
        'image': 'solar_protection.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Tailoring: Basic Mending': {
        'name': 'Tailoring: Basic Mending',
        'amount': 1,
        'image': 'tailoring_basic_mending.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Metallurgy: Basic Welding': {
        'name': 'Metallurgy: Basic Welding',
        'amount': 1,
        'image': 'metallurgy_basic_welding.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Additional Honing Materials',
        'rarity': 3
    },
    'Powder of Sage': {
        'name': 'Powder of Sage',
        'amount': 1,
        'image': 'powder_sage.webp',
        'category': 'Enhancement Material',
        'subcategory': 'Other Materials',
        'rarity': 3
    },
    '[Artillerist] Barrage Enhancement Engraving Recipe': {
        'name': '[Artillerist] Barrage Enhancement Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Artillerist] Firepower Enhancement Engraving Recipe': {
        'name': '[Artillerist] Firepower Enhancement Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Bard] Desperate Salvation Engraving Recipe': {
        'name': '[Bard] Desperate Salvation Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Bard] True Courage Engraving Recipe': {
        'name': '[Bard] True Courage Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Berserker] Berserker Technique Engraving Recipe': {
        'name': '[Berserker] Berserker Technique Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Berserker] Mayhem Engraving Recipe': {
        'name': '[Berserker] Mayhem Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Deadeye] Enhanced Weapon Engraving Recipe': {
        'name': '[Deadeye] Enhanced Weapon Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Deadeye] Pistoleer Engraving Recipe': {
        'name': '[Deadeye] Pistoleer Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Deathblade] Remaining Energy Engraving Recipe': {
        'name': '[Deathblade] Remaining Energy Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Deathblade] Surge Engraving Recipe': {
        'name': '[Deathblade] Surge Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Glaivier] Control Engraving Recipe': {
        'name': '[Glaivier] Control Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Glaivier] Pinnacle Engraving Recipe': {
        'name': '[Glaivier] Pinnacle Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Gunlancer] Combat Readiness Engraving Recipe': {
        'name': '[Gunlancer] Combat Readiness Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Gunlancer] Lone Knight Engraving Recipe': {
        'name': '[Gunlancer] Lone Knight Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Gunslinger] Peacemaker Engraving Recipe': {
        'name': '[Gunslinger] Peacemaker Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Gunslinger] Time to Hunt Engraving Recipe': {
        'name': '[Gunslinger] Time to Hunt Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Paladin] Blessed Aura Engraving Recipe': {
        'name': '[Paladin] Blessed Aura Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Paladin] Judgment Engraving Recipe': {
        'name': '[Paladin] Judgment Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Scrapper] Shock Training Engraving Recipe': {
        'name': '[Scrapper] Shock Training Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Scrapper] Ultimate Skill: Taijutsu Engraving Recipe': {
        'name': '[Scrapper] Ultimate Skill: Taijutsu Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Shadowhunter] Demonic Impulse Engraving Recipe': {
        'name': '[Shadowhunter] Demonic Impulse Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Shadowhunter] Perfect Suppression Engraving Recipe': {
        'name': '[Shadowhunter] Perfect Suppression Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Sharpshooter] Death Strike Engraving Recipe': {
        'name': '[Sharpshooter] Death Strike Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Sharpshooter] Loyal Companion Engraving Recipe': {
        'name': '[Sharpshooter] Loyal Companion Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Sorceress] Igniter Engraving Recipe': {
        'name': '[Sorceress] Igniter Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Sorceress] Reflux Engraving Recipe': {
        'name': '[Sorceress] Reflux Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Soulfist] Energy Overflow Engraving Recipe': {
        'name': '[Soulfist] Energy Overflow Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Soulfist] Robust Spirit Engraving Recipe': {
        'name': '[Soulfist] Robust Spirit Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Striker] Deathblow Engraving Recipe': {
        'name': '[Striker] Deathblow Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Striker] Esoteric Flurry Engraving Recipe': {
        'name': '[Striker] Esoteric Flurry Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Wardancer] Esoteric Skill Enhancement Engraving Recipe': {
        'name': '[Wardancer] Esoteric Skill Enhancement Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    '[Wardancer] First Intention Engraving Recipe': {
        'name': '[Wardancer] First Intention Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Adrenaline Engraving Recipe': {
        'name': 'Adrenaline Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'All-Out Attack Engraving Recipe': {
        'name': 'All-Out Attack Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Ambush Master Engraving Recipe': {
        'name': 'Ambush Master Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Awakening Engraving Recipe': {
        'name': 'Awakening Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Barricade Engraving Recipe': {
        'name': 'Barricade Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Battle Engraving Recipe': {
        'name': 'Battle Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Battle Engraving Recipe': {
        'name': 'Battle Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Broken Bone Engraving Recipe': {
        'name': 'Broken Bone Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Class Engraving Recipe': {
        'name': 'Class Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Contender Engraving Recipe': {
        'name': 'Contender Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Crisis Evasion Engraving Recipe': {
        'name': 'Crisis Evasion Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Crushing Fist Engraving Recipe': {
        'name': 'Crushing Fist Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Cursed Doll Engraving Recipe': {
        'name': 'Cursed Doll Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Disrespect Engraving Recipe': {
        'name': 'Disrespect Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Divine Protection Engraving Recipe': {
        'name': 'Divine Protection Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Drops of Ether Engraving Recipe': {
        'name': 'Drops of Ether Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Emergency Rescue Engraving Recipe': {
        'name': 'Emergency Rescue Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Enhanced Shield Engraving Recipe': {
        'name': 'Enhanced Shield Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Ether Predator Engraving Recipe': {
        'name': 'Ether Predator Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Expert Engraving Recipe': {
        'name': 'Expert Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Explosive Expert Engraving Recipe': {
        'name': 'Explosive Expert Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Fortitude Engraving Recipe': {
        'name': 'Fortitude Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Grudge Engraving Recipe': {
        'name': 'Grudge Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Heavy Armor Engraving Recipe': {
        'name': 'Heavy Armor Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Hit Master Engraving Recipe': {
        'name': 'Hit Master Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Keen Blunt Weapon Engraving Recipe': {
        'name': 'Keen Blunt Weapon Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Lightning Fury Engraving Recipe': {
        'name': 'Lightning Fury Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Magick Stream Engraving Recipe': {
        'name': 'Magick Stream Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Mass Increase Engraving Recipe': {
        'name': 'Mass Increase Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Master Brawler Engraving Recipe': {
        'name': 'Master Brawler Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Master of Escape Engraving Recipe': {
        'name': 'Master of Escape Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Master\'s Tenacity Engraving Recipe': {
        'name': 'Master\'s Tenacity Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Max MP Increase Engraving Recipe': {
        'name': 'Max MP Increase Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'MP Efficiency Increase Engraving Recipe': {
        'name': 'MP Efficiency Increase Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Necromancy Engraving Recipe': {
        'name': 'Necromancy Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Precise Dagger Engraving Recipe': {
        'name': 'Precise Dagger Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Preemptive Strike Engraving Recipe': {
        'name': 'Preemptive Strike Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Propulsion Engraving Recipe': {
        'name': 'Propulsion Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Raid Captain Engraving Recipe': {
        'name': 'Raid Captain Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Shield Piercing Engraving Recipe': {
        'name': 'Shield Piercing Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Sight Focus Engraving Recipe': {
        'name': 'Sight Focus Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Spirit Absorption Engraving Recipe': {
        'name': 'Spirit Absorption Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Stabilized Status Engraving Recipe': {
        'name': 'Stabilized Status Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Strong Will Engraving Recipe': {
        'name': 'Strong Will Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Super Charge Engraving Recipe': {
        'name': 'Super Charge Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Vital Point Hit Engraving Recipe': {
        'name': 'Vital Point Hit Engraving Recipe',
        'amount': 1,
        'category': 'Engraving Recipe',
        'subcategory': None
    },
    'Adrophine Potion': {
        'name': 'Adrophine Potion',
        'amount': 10,
        'image': 'adrophine_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 3
    },
    'Awakening Potion': {
        'name': 'Awakening Potion',
        'amount': 10,
        'image': 'awakening_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 3
    },
    'Marching Flag': {
        'name': 'Marching Flag',
        'amount': 10,
        'image': 'marching_flag.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 2
    },
    'Protective Potion': {
        'name': 'Protective Potion',
        'amount': 10,
        'image': 'protective_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 2
    },
    'Splendid Marching Flag': {
        'name': 'Splendid Marching Flag',
        'amount': 10,
        'image': 'splendid_marching_flag.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 2
    },
    'Splendid Protective Potion': {
        'name': 'Splendid Protective Potion',
        'amount': 10,
        'image': 'splendid_protective_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 2
    },
    'Splendid Swift Robe': {
        'name': 'Splendid Swift Robe',
        'amount': 10,
        'image': 'splendid_swift_robe.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 2
    },
    'Swiftness Robe': {
        'name': 'Swiftness Robe',
        'amount': 10,
        'image': 'swiftness_robe.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Buff',
        'rarity': 2
    },
    'Clay Grenade': {
        'name': 'Clay Grenade',
        'amount': 10,
        'image': 'clay_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Corrosive Bomb': {
        'name': 'Corrosive Bomb',
        'amount': 10,
        'image': 'corrosive_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Dark Grenade': {
        'name': 'Dark Grenade',
        'amount': 10,
        'image': 'dark_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Destruction Bomb': {
        'name': 'Destruction Bomb',
        'amount': 10,
        'image': 'destruction_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Electric Grenade': {
        'name': 'Electric Grenade',
        'amount': 10,
        'image': 'electric_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Flame Grenade': {
        'name': 'Flame Grenade',
        'amount': 10,
        'image': 'flame_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Flash Grenade': {
        'name': 'Flash Grenade',
        'amount': 10,
        'image': 'flash_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Frost Grenade': {
        'name': 'Frost Grenade',
        'amount': 10,
        'image': 'frost_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Pheromone Bomb': {
        'name': 'Pheromone Bomb',
        'amount': 10,
        'image': 'pheromone_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Sacred Bomb': {
        'name': 'Sacred Bomb',
        'amount': 10,
        'image': 'sacred_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Sleep Bomb': {
        'name': 'Sleep Bomb',
        'amount': 10,
        'image': 'sleep_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Clay Grenade': {
        'name': 'Splendid Clay Grenade',
        'amount': 10,
        'image': 'splendid_clay_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Corrosion Bomb': {
        'name': 'Splendid Corrosion Bomb',
        'amount': 10,
        'image': 'splendid_corrosion_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Dark Grenade': {
        'name': 'Splendid Dark Grenade',
        'amount': 10,
        'image': 'splendid_dark_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Destruction Bomb': {
        'name': 'Splendid Destruction Bomb',
        'amount': 10,
        'image': 'splendid_destruction_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Flame Grenade': {
        'name': 'Splendid Flame Grenade',
        'amount': 10,
        'image': 'splendid_flame_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Flash Grenade': {
        'name': 'Splendid Flash Grenade',
        'amount': 10,
        'image': 'splendid_flash_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Frost Grenade': {
        'name': 'Splendid Frost Grenade',
        'amount': 10,
        'image': 'splendid_frost_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Lightening Grenade': {
        'name': 'Splendid Lightening Grenade',
        'amount': 10,
        'image': 'splendid_lightening_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Sacred Bomb': {
        'name': 'Splendid Sacred Bomb',
        'amount': 10,
        'image': 'splendid_sacred_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Sleep Bomb': {
        'name': 'Splendid Sleep Bomb',
        'amount': 10,
        'image': 'splendid_sleep_bomb.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Thunder Potion': {
        'name': 'Splendid Thunder Potion',
        'amount': 10,
        'image': 'splendid_thunder_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Splendid Whirlwind Grenade': {
        'name': 'Splendid Whirlwind Grenade',
        'amount': 10,
        'image': 'splendid_whirlwind_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Thunder Potion': {
        'name': 'Thunder Potion',
        'amount': 10,
        'image': 'thunder_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Whirlwind Grenade': {
        'name': 'Whirlwind Grenade',
        'amount': 10,
        'image': 'whirlwind_grenade.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Offense',
        'rarity': 2
    },
    'Elemental HP Potion': {
        'name': 'Elemental HP Potion',
        'amount': 10,
        'image': 'elemental_hp_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Recovery',
        'rarity': 3
    },
    'Splendid Elemental HP Potion': {
        'name': 'Splendid Elemental HP Potion',
        'amount': 10,
        'image': 'splendid_elemental_hp_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Recovery',
        'rarity': 3
    },
    'Major HP Potion': {
        'name': 'Major HP Potion',
        'amount': 10,
        'image': 'major_hp_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Recovery',
        'rarity': 2
    },
    'HP Potion': {
        'name': 'HP Potion',
        'amount': 10,
        'image': 'hp_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Recovery',
        'rarity': 1
    },
    'Luterra\'s Horn': {
        'name': 'Luterra\'s Horn',
        'amount': 10,
        'image': 'luterras_horn.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 3
    },
    'Splendid Stealth Robe': {
        'name': 'Splendid Stealth Robe',
        'amount': 10,
        'image': 'splendid_stealth_robe.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 3
    },
    'Stealth Robe': {
        'name': 'Stealth Robe',
        'amount': 10,
        'image': 'stealth_robe.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 3
    },
    'Time Stop Potion': {
        'name': 'Time Stop Potion',
        'amount': 10,
        'image': 'time_stop_potion.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 3
    },
    'Camouflage Robe': {
        'name': 'Camouflage Robe',
        'amount': 10,
        'image': 'camouflage_robe.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Campfire': {
        'name': 'Campfire',
        'amount': 10,
        'image': 'campfire.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Panacea': {
        'name': 'Panacea',
        'amount': 10,
        'image': 'panacea.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Repair Shop Portal Scroll': {
        'name': 'Repair Shop Portal Scroll',
        'amount': 10,
        'image': 'repair_shop_portal_scroll.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Sacred Charm': {
        'name': 'Sacred Charm',
        'amount': 10,
        'image': 'sacred_charm.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Splendid Campfire': {
        'name': 'Splendid Campfire',
        'amount': 10,
        'image': 'splendid_campfire.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Splendid Disguise Robe': {
        'name': 'Splendid Disguise Robe',
        'amount': 10,
        'image': 'splendid_disguise_robe.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Splendid Panacea': {
        'name': 'Splendid Panacea',
        'amount': 10,
        'image': 'splendid_panacea.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Splendid Sacred Charm': {
        'name': 'Splendid Sacred Charm',
        'amount': 10,
        'image': 'splendid_sacred_charm.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Splendid Taunting Scarecrow': {
        'name': 'Splendid Taunting Scarecrow',
        'amount': 10,
        'image': 'splendid_taunting_scarecrow.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Taunting Scarecrow': {
        'name': 'Taunting Scarecrow',
        'amount': 10,
        'image': 'taunting_scarecrow.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 2
    },
    'Flare': {
        'name': 'Flare',
        'amount': 10,
        'image': 'flare.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 1
    },
    'Splendid Flare': {
        'name': 'Splendid Flare',
        'amount': 10,
        'image': 'splendid_flare.webp',
        'category': 'Combat Supplies',
        'subcategory': 'Battle Item - Utility',
        'rarity': 1
    },
    'Magical Vernese Brandy': {
        'name': 'Magical Vernese Brandy',
        'rarity': 5,
        'image': 'magical-vernese-brandy.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Vernese Brisket': {
        'name': 'Vernese Brisket',
        'rarity': 5,
        'image': 'vernese-brisket.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    '500-year-old Mera Wine': {
        'name': '500-year-old Mera Wine',
        'rarity': 4,
        'image': '500-year-old-mera-wine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bergstrom Drink': {
        'name': 'Bergstrom Drink',
        'rarity': 4,
        'image': 'bergstrom-drink.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bloody Fist': {
        'name': 'Bloody Fist',
        'rarity': 4,
        'image': 'bloody-fist.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Crayfish with Vegetables': {
        'name': 'Crayfish with Vegetables',
        'rarity': 4,
        'image': 'crayfish-with-vegetables.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Crumpled Letter': {
        'name': 'Crumpled Letter',
        'rarity': 4,
        'image': 'crumpled-letter.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Crunch Crunch Fried Shell': {
        'name': 'Crunch Crunch Fried Shell',
        'rarity': 4,
        'image': 'crunch-crunch-fried-shell.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Donut Maiden': {
        'name': 'Donut Maiden',
        'rarity': 4,
        'image': 'donut-maiden.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Eel Caviar Salad': {
        'name': 'Eel Caviar Salad',
        'rarity': 4,
        'image': 'eel-caviar-salad.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fully-melted Gelato': {
        'name': 'Fully-melted Gelato',
        'rarity': 4,
        'image': 'fully-melted-gelato.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Gourmet Stir-fried Mushroom': {
        'name': 'Gourmet Stir-fried Mushroom',
        'rarity': 4,
        'image': 'gourmet-stir-fried-mushroom.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Great Stew': {
        'name': 'Great Stew',
        'rarity': 4,
        'image': 'great-stew.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Half and Half, Dip and Pour': {
        'name': 'Half and Half, Dip and Pour',
        'rarity': 4,
        'image': 'half-and-half,-dip-and-pour.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Harmony': {
        'name': 'Harmony',
        'rarity': 4,
        'image': 'harmony.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Holy Potato with Teeth Marks': {
        'name': 'Holy Potato with Teeth Marks',
        'rarity': 4,
        'image': 'holy-potato-with-teeth-marks.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Krakan Intestine Cream Soup': {
        'name': 'Krakan Intestine Cream Soup',
        'rarity': 4,
        'image': 'krakan-intestine-cream-soup.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Long Live the Queen!': {
        'name': 'Long Live the Queen!',
        'rarity': 4,
        'image': 'long-live-the-queen.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Medrick Hair Loss Solution': {
        'name': 'Medrick Hair Loss Solution',
        'rarity': 4,
        'image': 'medrick-hair-loss-solution.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Perfect Sugar Sculpture': {
        'name': 'Perfect Sugar Sculpture',
        'rarity': 4,
        'image': 'perfect-sugar-sculpture.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Punika Festival\'s Dish': {
        'name': 'Punika Festival\'s Dish',
        'rarity': 4,
        'image': 'punika-festival-s-dish.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Rainmaking Ritual Food': {
        'name': 'Rainmaking Ritual Food',
        'rarity': 4,
        'image': 'rainmaking-ritual-food.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Rainmaking Ritual Leftovers': {
        'name': 'Rainmaking Ritual Leftovers',
        'rarity': 4,
        'image': 'rainmaking-ritual-leftovers.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Salt Cracker': {
        'name': 'Salt Cracker',
        'rarity': 4,
        'image': 'salt-cracker.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Shushire Snowflake Shaved Ice': {
        'name': 'Shushire Snowflake Shaved Ice',
        'rarity': 4,
        'image': 'shushire-snowflake-shaved-ice.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sirius\'s Tears': {
        'name': 'Sirius\'s Tears',
        'rarity': 4,
        'image': 'sirius-s-tears.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Snail Roll Cake': {
        'name': 'Snail Roll Cake',
        'rarity': 4,
        'image': 'snail-roll-cake.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Soup of Transcendence': {
        'name': 'Soup of Transcendence',
        'rarity': 4,
        'image': 'soup-of-transcendence.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Steamed Papu Crab': {
        'name': 'Steamed Papu Crab',
        'rarity': 4,
        'image': 'steamed-papu-crab.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Tooki Tooki Soup': {
        'name': 'Tooki Tooki Soup',
        'rarity': 4,
        'image': 'tooki-tooki-soup.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Unknown Liquid XD-6353': {
        'name': 'Unknown Liquid XD-6353',
        'rarity': 4,
        'image': 'unknown-liquid-xd-6353.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Vernilaya': {
        'name': 'Vernilaya',
        'rarity': 4,
        'image': 'vernilaya.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Wild Banana Bread': {
        'name': 'Wild Banana Bread',
        'rarity': 4,
        'image': 'wild-banana-bread.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Worm Head Jelly': {
        'name': 'Worm Head Jelly',
        'rarity': 4,
        'image': 'worm-head-jelly.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Wriggling Tentacle Sashimi': {
        'name': 'Wriggling Tentacle Sashimi',
        'rarity': 4,
        'image': 'wriggling-tentacle-sashimi.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Zechbas': {
        'name': 'Zechbas',
        'rarity': 4,
        'image': 'zechbas.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Age-old Encavian Wine': {
        'name': 'Age-old Encavian Wine',
        'rarity': 3,
        'image': 'age-old-encavian-wine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Almost Complete Distilled Beverage': {
        'name': 'Almost Complete Distilled Beverage',
        'rarity': 3,
        'image': 'almost-complete-distilled-beverage.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Avesta List': {
        'name': 'Avesta List',
        'rarity': 3,
        'image': 'avesta-list.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Avesta Smoked Beef Jerkey': {
        'name': 'Avesta Smoked Beef Jerkey',
        'rarity': 3,
        'image': 'avesta-smoked-beef-jerkey.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Balankar Ranger\'s Salad': {
        'name': 'Balankar Ranger\'s Salad',
        'rarity': 3,
        'image': 'balankar-ranger-s-salad.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bear Gallbladder Skewer': {
        'name': 'Bear Gallbladder Skewer',
        'rarity': 3,
        'image': 'bear-gallbladder-skewer.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bellion Wings': {
        'name': 'Bellion Wings',
        'rarity': 3,
        'image': 'bellion-wings.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Biography of Galatur': {
        'name': 'Biography of Galatur',
        'rarity': 3,
        'image': 'biography-of-galatur.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Black Fox Flag': {
        'name': 'Black Fox Flag',
        'rarity': 3,
        'image': 'black-fox-flag.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bloodstained Rod': {
        'name': 'Bloodstained Rod',
        'rarity': 3,
        'image': 'bloodstained-rod.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Boar BBQ': {
        'name': 'Boar BBQ',
        'rarity': 3,
        'image': 'boar-bbq.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Boosting Fluid Soup': {
        'name': 'Boosting Fluid Soup',
        'rarity': 3,
        'image': 'boosting-fluid-soup.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Brisket Ready to Be Applied with Rub': {
        'name': 'Brisket Ready to Be Applied with Rub',
        'rarity': 3,
        'image': 'brisket-ready-to-be-applied-with-rub.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Broken Sugar Sculpture': {
        'name': 'Broken Sugar Sculpture',
        'rarity': 3,
        'image': 'broken-sugar-sculpture.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Cashew Cashew Smoothie': {
        'name': 'Cashew Cashew Smoothie',
        'rarity': 3,
        'image': 'cashew-cashew-smoothie.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Cashew Fruit': {
        'name': 'Cashew Fruit',
        'rarity': 3,
        'image': 'cashew-fruit.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Clotted Blood of Rakathus': {
        'name': 'Clotted Blood of Rakathus',
        'rarity': 3,
        'image': 'clotted-blood-of-rakathus.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Coolkur Beer': {
        'name': 'Coolkur Beer',
        'rarity': 3,
        'image': 'coolkur-beer.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Cykin Combat Ration Type A': {
        'name': 'Cykin Combat Ration Type A',
        'rarity': 3,
        'image': 'cykin-combat-ration-type-a.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Cykin Combat Ration Type C': {
        'name': 'Cykin Combat Ration Type C',
        'rarity': 3,
        'image': 'cykin-combat-ration-type-c.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Deer Hind Hooves Stew': {
        'name': 'Deer Hind Hooves Stew',
        'rarity': 3,
        'image': 'deer-hind-hooves-stew.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Dusty Rainbow Candy': {
        'name': 'Dusty Rainbow Candy',
        'rarity': 3,
        'image': 'dusty-rainbow-candy.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Eel Herb Kholodets': {
        'name': 'Eel Herb Kholodets',
        'rarity': 3,
        'image': 'eel-herb-kholodets.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Efferin\'s Egg Rice': {
        'name': 'Efferin\'s Egg Rice',
        'rarity': 3,
        'image': 'efferin-s-egg-rice.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Eggy Eggy Soft Boiled Egg': {
        'name': 'Eggy Eggy Soft Boiled Egg',
        'rarity': 3,
        'image': 'eggy-eggy-soft-boiled-egg.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Encrypted Note': {
        'name': 'Encrypted Note',
        'rarity': 3,
        'image': 'encrypted-note.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Ether Essence': {
        'name': 'Ether Essence',
        'rarity': 3,
        'image': 'ether-essence.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Feiton Blood Pudding Sausage': {
        'name': 'Feiton Blood Pudding Sausage',
        'rarity': 3,
        'image': 'feiton-blood-pudding-sausage.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fesnar Mushroom Stew': {
        'name': 'Fesnar Mushroom Stew',
        'rarity': 3,
        'image': 'fesnar-mushroom-stew.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Flower Salad': {
        'name': 'Flower Salad',
        'rarity': 3,
        'image': 'flower-salad.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Foundation Centennial Wine': {
        'name': 'Foundation Centennial Wine',
        'rarity': 3,
        'image': 'foundation-centennial-wine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Frost Spider Egg': {
        'name': 'Frost Spider Egg',
        'rarity': 3,
        'image': 'frost-spider-egg.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Frozen Butterfly Larva': {
        'name': 'Frozen Butterfly Larva',
        'rarity': 3,
        'image': 'frozen-butterfly-larva.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Giant Flower Petals': {
        'name': 'Giant Flower Petals',
        'rarity': 3,
        'image': 'giant-flower-petals.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Goblin Fish Soup': {
        'name': 'Goblin Fish Soup',
        'rarity': 3,
        'image': 'goblin-fish-soup.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Gourmet Seafood Stew': {
        'name': 'Gourmet Seafood Stew',
        'rarity': 3,
        'image': 'gourmet-seafood-stew.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Grilled Sapphire Sardine': {
        'name': 'Grilled Sapphire Sardine',
        'rarity': 3,
        'image': 'grilled-sapphire-sardine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Jelly Chew': {
        'name': 'Jelly Chew',
        'rarity': 3,
        'image': 'jelly-chew.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Kaloa Boar BBQ': {
        'name': 'Kaloa Boar BBQ',
        'rarity': 3,
        'image': 'kaloa-boar-bbq.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Kandarian Cold Lager': {
        'name': 'Kandarian Cold Lager',
        'rarity': 3,
        'image': 'kandarian-cold-lager.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Lakebar Freshwater Fish Stew': {
        'name': 'Lakebar Freshwater Fish Stew',
        'rarity': 3,
        'image': 'lakebar-freshwater-fish-stew.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Lucky Fortune Cookie': {
        'name': 'Lucky Fortune Cookie',
        'rarity': 3,
        'image': 'lucky-fortune-cookie.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Luterran Course Meal': {
        'name': 'Luterran Course Meal',
        'rarity': 3,
        'image': 'luterran-course-meal.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Lynnis\'s Ring': {
        'name': 'Lynnis\'s Ring',
        'rarity': 3,
        'image': 'lynnis-s-ring.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Manpo\'s Secret Meat Dumpling': {
        'name': 'Manpo\'s Secret Meat Dumpling',
        'rarity': 3,
        'image': 'manpo-s-secret-meat-dumpling.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Meat Bug': {
        'name': 'Meat Bug',
        'rarity': 3,
        'image': 'meat-bug.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Mine Car Lunchbox': {
        'name': 'Mine Car Lunchbox',
        'rarity': 3,
        'image': 'mine-car-lunchbox.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Miner\'s Rum': {
        'name': 'Miner\'s Rum',
        'rarity': 3,
        'image': 'miner-s-rum.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Natural Mungka Jerky': {
        'name': 'Natural Mungka Jerky',
        'rarity': 3,
        'image': 'natural-mungka-jerky.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Neria\'s Cheese Snack': {
        'name': 'Neria\'s Cheese Snack',
        'rarity': 3,
        'image': 'neria-s-cheese-snack.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Nomadic Dream': {
        'name': 'Nomadic Dream',
        'rarity': 3,
        'image': 'nomadic-dream.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Old Canned Food': {
        'name': 'Old Canned Food',
        'rarity': 3,
        'image': 'old-canned-food.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Pit-A-Pat Macaron': {
        'name': 'Pit-A-Pat Macaron',
        'rarity': 3,
        'image': 'pit-a-pat-macaron.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Plenty Plenty Mokoko Gift Package': {
        'name': 'Plenty Plenty Mokoko Gift Package',
        'rarity': 3,
        'image': 'plenty-plenty-mokoko-gift-package.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Pocket Watch of Dawn': {
        'name': 'Pocket Watch of Dawn',
        'rarity': 3,
        'image': 'pocket-watch-of-dawn.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Pow Pow Honey Health Tonic': {
        'name': 'Pow Pow Honey Health Tonic',
        'rarity': 3,
        'image': 'pow-pow-honey-health-tonic.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Protein Packed White Bird Stew': {
        'name': 'Protein Packed White Bird Stew',
        'rarity': 3,
        'image': 'protein-packed-white-bird-stew.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Proxima Course Meal': {
        'name': 'Proxima Course Meal',
        'rarity': 3,
        'image': 'proxima-course-meal.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Regria Flower Oil': {
        'name': 'Regria Flower Oil',
        'rarity': 3,
        'image': 'regria-flower-oil.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Regria Wheat Bread': {
        'name': 'Regria Wheat Bread',
        'rarity': 3,
        'image': 'regria-wheat-bread.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Ryucrokota Salo': {
        'name': 'Ryucrokota Salo',
        'rarity': 3,
        'image': 'ryucrokota-salo.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Salt-grilled Saltbug': {
        'name': 'Salt-grilled Saltbug',
        'rarity': 3,
        'image': 'salt-grilled-saltbug.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Salted Food Box': {
        'name': 'Salted Food Box',
        'rarity': 3,
        'image': 'salted-food-box.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sand in a Bottle': {
        'name': 'Sand in a Bottle',
        'rarity': 3,
        'image': 'sand-in-a-bottle.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sceptrumpam 3mg': {
        'name': 'Sceptrumpam 3mg',
        'rarity': 3,
        'image': 'sceptrumpam-3mg.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Secret Pill of Jeok Family': {
        'name': 'Secret Pill of Jeok Family',
        'rarity': 3,
        'image': 'secret-pill-of-jeok-family.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Secret Yeon-Style Marinated Special': {
        'name': 'Secret Yeon-Style Marinated Special',
        'rarity': 3,
        'image': 'secret-yeon-style-marinated-special.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Solar Knights Token': {
        'name': 'Solar Knights Token',
        'rarity': 3,
        'image': 'solar-knights-token.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Solar Stone': {
        'name': 'Solar Stone',
        'rarity': 3,
        'image': 'solar-stone.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Solar Tree Sprout Cider': {
        'name': 'Solar Tree Sprout Cider',
        'rarity': 3,
        'image': 'solar-tree-sprout-cider.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Song Inscribed Stone': {
        'name': 'Song Inscribed Stone',
        'rarity': 3,
        'image': 'song-inscribed-stone.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sparkling Elemental Food': {
        'name': 'Sparkling Elemental Food',
        'rarity': 3,
        'image': 'sparkling-elemental-food.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Starsand Cocktail': {
        'name': 'Starsand Cocktail',
        'rarity': 3,
        'image': 'starsand-cocktail.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Steamed Oyster with White Wine': {
        'name': 'Steamed Oyster with White Wine',
        'rarity': 3,
        'image': 'steamed-oyster-with-white-wine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sweet Honey Butter Beer': {
        'name': 'Sweet Honey Butter Beer',
        'rarity': 3,
        'image': 'sweet-honey-butter-beer.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sweet Sweet Royal Jelly': {
        'name': 'Sweet Sweet Royal Jelly',
        'rarity': 3,
        'image': 'sweet-sweet-royal-jelly.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Thirain T-Bone Steak': {
        'name': 'Thirain T-Bone Steak',
        'rarity': 3,
        'image': 'thirain-t-bone-steak.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Veda\'s Prideholme-style Home Food': {
        'name': 'Veda\'s Prideholme-style Home Food',
        'rarity': 3,
        'image': 'veda-s-prideholme-style-home-food.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Vern Anniversary Spirits': {
        'name': 'Vern Anniversary Spirits',
        'rarity': 3,
        'image': 'vern-anniversary-spirits.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Wolf Meat': {
        'name': 'Wolf Meat',
        'rarity': 3,
        'image': 'wolf-meat.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Wonderful Rum': {
        'name': 'Wonderful Rum',
        'rarity': 3,
        'image': 'wonderful-rum.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Worm Poop Coffee': {
        'name': 'Worm Poop Coffee',
        'rarity': 3,
        'image': 'worm-poop-coffee.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'X-090892': {
        'name': 'X-090892',
        'rarity': 3,
        'image': 'x-090892.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    '499-year-old Mera Wine': {
        'name': '499-year-old Mera Wine',
        'rarity': 2,
        'image': '499-year-old-mera-wine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Adrinne\'s Ring': {
        'name': 'Adrinne\'s Ring',
        'rarity': 2,
        'image': 'adrinne-s-ring.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Adventurer\'s Journal': {
        'name': 'Adventurer\'s Journal',
        'rarity': 2,
        'image': 'adventurer-s-journal.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Aquilok Skin': {
        'name': 'Aquilok Skin',
        'rarity': 2,
        'image': 'aquilok-skin.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bergstrom\'s Invisibility Potion': {
        'name': 'Bergstrom\'s Invisibility Potion',
        'rarity': 2,
        'image': 'bergstrom-s-invisibility-potion.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bergstrom\'s Yellow Potion': {
        'name': 'Bergstrom\'s Yellow Potion',
        'rarity': 2,
        'image': 'bergstrom-s-yellow-potion.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Boiling Liquid': {
        'name': 'Boiling Liquid',
        'rarity': 2,
        'image': 'boiling-liquid.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Bread Crumbs': {
        'name': 'Bread Crumbs',
        'rarity': 2,
        'image': 'bread-crumbs.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Brisket, Ready for Dry Rub': {
        'name': 'Brisket, Ready for Dry Rub',
        'rarity': 2,
        'image': 'brisket,-ready-for-dry-rub.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Collected Stories of the Luterran Knights': {
        'name': 'Collected Stories of the Luterran Knights',
        'rarity': 2,
        'image': 'collected-stories-of-the-luterran-knights.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Crow Stone': {
        'name': 'Crow Stone',
        'rarity': 2,
        'image': 'crow-stone.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Dagger of the High Priest': {
        'name': 'Dagger of the High Priest',
        'rarity': 2,
        'image': 'dagger-of-the-high-priest.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Donut Butler': {
        'name': 'Donut Butler',
        'rarity': 2,
        'image': 'donut-butler.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Donut Servant': {
        'name': 'Donut Servant',
        'rarity': 2,
        'image': 'donut-servant.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Enviska\'s Talisman': {
        'name': 'Enviska\'s Talisman',
        'rarity': 2,
        'image': 'enviska-s-talisman.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fabulous Saucer': {
        'name': 'Fabulous Saucer',
        'rarity': 2,
        'image': 'fabulous-saucer.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Failed Distilled Beverage': {
        'name': 'Failed Distilled Beverage',
        'rarity': 2,
        'image': 'failed-distilled-beverage.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fake Beard': {
        'name': 'Fake Beard',
        'rarity': 2,
        'image': 'fake-beard.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fiend Mask': {
        'name': 'Fiend Mask',
        'rarity': 2,
        'image': 'fiend-mask.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Food Chest for Trade': {
        'name': 'Food Chest for Trade',
        'rarity': 2,
        'image': 'food-chest-for-trade.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fortune Cookie Chest': {
        'name': 'Fortune Cookie Chest',
        'rarity': 2,
        'image': 'fortune-cookie-chest.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fresh Blood of the Corrupted': {
        'name': 'Fresh Blood of the Corrupted',
        'rarity': 2,
        'image': 'fresh-blood-of-the-corrupted.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Fresh Cocktail': {
        'name': 'Fresh Cocktail',
        'rarity': 2,
        'image': 'fresh-cocktail.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Gelato': {
        'name': 'Gelato',
        'rarity': 2,
        'image': 'gelato.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Glyphed Stone': {
        'name': 'Glyphed Stone',
        'rarity': 2,
        'image': 'glyphed-stone.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Haal Ruins Research Journal': {
        'name': 'Haal Ruins Research Journal',
        'rarity': 2,
        'image': 'haal-ruins-research-journal.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Honey Butter Beer': {
        'name': 'Honey Butter Beer',
        'rarity': 2,
        'image': 'honey-butter-beer.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Hot Chocolate Coffee': {
        'name': 'Hot Chocolate Coffee',
        'rarity': 2,
        'image': 'hot-chocolate-coffee.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Legendary Drinkers Daily': {
        'name': 'Legendary Drinkers Daily',
        'rarity': 2,
        'image': 'legendary-drinkers-daily.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Levatanos Core': {
        'name': 'Levatanos Core',
        'rarity': 2,
        'image': 'levatanos-core.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Marionette of the Steel Lady': {
        'name': 'Marionette of the Steel Lady',
        'rarity': 2,
        'image': 'marionette-of-the-steel-lady.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Melting Gelato': {
        'name': 'Melting Gelato',
        'rarity': 2,
        'image': 'melting-gelato.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Nia Tribe Dream Decoration': {
        'name': 'Nia Tribe Dream Decoration',
        'rarity': 2,
        'image': 'nia-tribe-dream-decoration.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Not Fully Fermented Ryucrokota Salo': {
        'name': 'Not Fully Fermented Ryucrokota Salo',
        'rarity': 2,
        'image': 'not-fully-fermented-ryucrokota-salo.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Palatable Cocktail': {
        'name': 'Palatable Cocktail',
        'rarity': 2,
        'image': 'palatable-cocktail.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Portal Stone': {
        'name': 'Portal Stone',
        'rarity': 2,
        'image': 'portal-stone.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Promotional Flyer of the Verdantier': {
        'name': 'Promotional Flyer of the Verdantier',
        'rarity': 2,
        'image': 'promotional-flyer-of-the-verdantier.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Proxima Root Nugget': {
        'name': 'Proxima Root Nugget',
        'rarity': 2,
        'image': 'proxima-root-nugget.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Proxima Salad': {
        'name': 'Proxima Salad',
        'rarity': 2,
        'image': 'proxima-salad.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Pungent Cocktail': {
        'name': 'Pungent Cocktail',
        'rarity': 2,
        'image': 'pungent-cocktail.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Pungent Scale': {
        'name': 'Pungent Scale',
        'rarity': 2,
        'image': 'pungent-scale.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Questionable Cocktail': {
        'name': 'Questionable Cocktail',
        'rarity': 2,
        'image': 'questionable-cocktail.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Questionable Sugar Sculpture': {
        'name': 'Questionable Sugar Sculpture',
        'rarity': 2,
        'image': 'questionable-sugar-sculpture.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Report on Heavy Walker': {
        'name': 'Report on Heavy Walker',
        'rarity': 2,
        'image': 'report-on-heavy-walker.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Ripening Anti Hair Loss Agent': {
        'name': 'Ripening Anti Hair Loss Agent',
        'rarity': 2,
        'image': 'ripening-anti-hair-loss-agent.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Royal Warning': {
        'name': 'Royal Warning',
        'rarity': 2,
        'image': 'royal-warning.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Salt Crystal': {
        'name': 'Salt Crystal',
        'rarity': 2,
        'image': 'salt-crystal.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Salttree Fruit': {
        'name': 'Salttree Fruit',
        'rarity': 2,
        'image': 'salttree-fruit.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sapphire Sardine': {
        'name': 'Sapphire Sardine',
        'rarity': 2,
        'image': 'sapphire-sardine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sealing Charm': {
        'name': 'Sealing Charm',
        'rarity': 2,
        'image': 'sealing-charm.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Secret Ledger': {
        'name': 'Secret Ledger',
        'rarity': 2,
        'image': 'secret-ledger.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Snowflake Shaved Ice': {
        'name': 'Snowflake Shaved Ice',
        'rarity': 2,
        'image': 'snowflake-shaved-ice.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Somewhat Complete Distilled Beverage': {
        'name': 'Somewhat Complete Distilled Beverage',
        'rarity': 2,
        'image': 'somewhat-complete-distilled-beverage.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Special Potato': {
        'name': 'Special Potato',
        'rarity': 2,
        'image': 'special-potato.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'The Legend of King Luterra': {
        'name': 'The Legend of King Luterra',
        'rarity': 2,
        'image': 'the-legend-of-king-luterra.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Timeworn Blade of a Fighter': {
        'name': 'Timeworn Blade of a Fighter',
        'rarity': 2,
        'image': 'timeworn-blade-of-a-fighter.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Unlucky Fortune Cookie': {
        'name': 'Unlucky Fortune Cookie',
        'rarity': 2,
        'image': 'unlucky-fortune-cookie.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Yucky Yucky Hard Boiled Egg': {
        'name': 'Yucky Yucky Hard Boiled Egg',
        'rarity': 2,
        'image': 'yucky-yucky-hard-boiled-egg.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Avesta Journal': {
        'name': 'Avesta Journal',
        'rarity': 1,
        'image': 'avesta-journal.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Avesta\'s Red Cloth': {
        'name': 'Avesta\'s Red Cloth',
        'rarity': 1,
        'image': 'avesta-s-red-cloth.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Book of the Priest': {
        'name': 'Book of the Priest',
        'rarity': 1,
        'image': 'book-of-the-priest.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Brisket Ready to Be Applied with Rub': {
        'name': 'Brisket Ready to Be Applied with Rub',
        'rarity': 1,
        'image': 'brisket-ready-to-be-applied-with-rub.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Elzowin\'s Branch': {
        'name': 'Elzowin\'s Branch',
        'rarity': 1,
        'image': 'elzowin-s-branch.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Frost Spider Cocoon': {
        'name': 'Frost Spider Cocoon',
        'rarity': 1,
        'image': 'frost-spider-cocoon.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Gold Coin of the Dead': {
        'name': 'Gold Coin of the Dead',
        'rarity': 1,
        'image': 'gold-coin-of-the-dead.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Gold Coin of Vrad': {
        'name': 'Gold Coin of Vrad',
        'rarity': 1,
        'image': 'gold-coin-of-vrad.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Grangor\'s Tooth': {
        'name': 'Grangor\'s Tooth',
        'rarity': 1,
        'image': 'grangor-s-tooth.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Grey Bait Material': {
        'name': 'Grey Bait Material',
        'rarity': 1,
        'image': 'grey-bait-material.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Guardian\'s Record': {
        'name': 'Guardian\'s Record',
        'rarity': 1,
        'image': 'guardian-s-record.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Holy Book of Sceptrum': {
        'name': 'Holy Book of Sceptrum',
        'rarity': 1,
        'image': 'holy-book-of-sceptrum.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Hoyte News': {
        'name': 'Hoyte News',
        'rarity': 1,
        'image': 'hoyte-news.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Legend of Luoden River': {
        'name': 'Legend of Luoden River',
        'rarity': 1,
        'image': 'legend-of-luoden-river.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Nightmare Elixir': {
        'name': 'Nightmare Elixir',
        'rarity': 1,
        'image': 'nightmare-elixir.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Orange Bait Material': {
        'name': 'Orange Bait Material',
        'rarity': 1,
        'image': 'orange-bait-material.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Pendant of the Fallen Noble': {
        'name': 'Pendant of the Fallen Noble',
        'rarity': 1,
        'image': 'pendant-of-the-fallen-noble.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Prophet\'s Note': {
        'name': 'Prophet\'s Note',
        'rarity': 1,
        'image': 'prophet-s-note.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Punika Gin': {
        'name': 'Punika Gin',
        'rarity': 1,
        'image': 'punika-gin.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Ramella\'s Mirror': {
        'name': 'Ramella\'s Mirror',
        'rarity': 1,
        'image': 'ramella-s-mirror.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Red Bait Material': {
        'name': 'Red Bait Material',
        'rarity': 1,
        'image': 'red-bait-material.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Redhand Mercenary Gloves': {
        'name': 'Redhand Mercenary Gloves',
        'rarity': 1,
        'image': 'redhand-mercenary-gloves.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Research Note on Sapira': {
        'name': 'Research Note on Sapira',
        'rarity': 1,
        'image': 'research-note-on-sapira.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Roasted Banana Powder': {
        'name': 'Roasted Banana Powder',
        'rarity': 1,
        'image': 'roasted-banana-powder.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Smelly Boots': {
        'name': 'Smelly Boots',
        'rarity': 1,
        'image': 'smelly-boots.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Smelly Boots Chest': {
        'name': 'Smelly Boots Chest',
        'rarity': 1,
        'image': 'smelly-boots-chest.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Smelly Cheese Chest': {
        'name': 'Smelly Cheese Chest',
        'rarity': 1,
        'image': 'smelly-cheese-chest.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Starlight Conch Shell': {
        'name': 'Starlight Conch Shell',
        'rarity': 1,
        'image': 'starlight-conch-shell.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sugar Lump': {
        'name': 'Sugar Lump',
        'rarity': 1,
        'image': 'sugar-lump.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Sweet Mojito': {
        'name': 'Sweet Mojito',
        'rarity': 1,
        'image': 'sweet-mojito.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'The Origin of Tortoyk': {
        'name': 'The Origin of Tortoyk',
        'rarity': 1,
        'image': 'the-origin-of-tortoyk.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'The Secrets of Anikka Cuisine': {
        'name': 'The Secrets of Anikka Cuisine',
        'rarity': 1,
        'image': 'the-secrets-of-anikka-cuisine.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Thick Parchment': {
        'name': 'Thick Parchment',
        'rarity': 1,
        'image': 'thick-parchment.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Tome of the Horizon': {
        'name': 'Tome of the Horizon',
        'rarity': 1,
        'image': 'tome-of-the-horizon.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Valaire\'s Love Poet': {
        'name': 'Valaire\'s Love Poet',
        'rarity': 1,
        'image': 'valaire-s-love-poet.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Wanted Poster': {
        'name': 'Wanted Poster',
        'rarity': 1,
        'image': 'wanted-poster.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Wishlight': {
        'name': 'Wishlight',
        'rarity': 1,
        'image': 'wishlight.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Wood Blood': {
        'name': 'Wood Blood',
        'rarity': 1,
        'image': 'wood-blood.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Amalone\'s Journal': {
        'name': 'Amalone\'s Journal',
        'rarity': 0,
        'image': 'amalone-s-journal.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Armor Piece of a Knight': {
        'name': 'Armor Piece of a Knight',
        'rarity': 0,
        'image': 'armor-piece-of-a-knight.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Caldarr\'s Helm': {
        'name': 'Caldarr\'s Helm',
        'rarity': 0,
        'image': 'caldarr-s-helm.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Centurion\'s Notebook': {
        'name': 'Centurion\'s Notebook',
        'rarity': 0,
        'image': 'centurion-s-notebook.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Eagle Ring': {
        'name': 'Eagle Ring',
        'rarity': 0,
        'image': 'eagle-ring.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Help Wanted Poster': {
        'name': 'Help Wanted Poster',
        'rarity': 0,
        'image': 'help-wanted-poster.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Hybee Honey': {
        'name': 'Hybee Honey',
        'rarity': 0,
        'image': 'hybee-honey.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Icewing': {
        'name': 'Icewing',
        'rarity': 0,
        'image': 'icewing.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Illustrated Book of Ancient Elementals': {
        'name': 'Illustrated Book of Ancient Elementals',
        'rarity': 0,
        'image': 'illustrated-book-of-ancient-elementals.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Mari\'s Mechanical Doll': {
        'name': 'Mari\'s Mechanical Doll',
        'rarity': 0,
        'image': 'mari-s-mechanical-doll.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Mark of the Holy Sacrian Empire': {
        'name': 'Mark of the Holy Sacrian Empire',
        'rarity': 0,
        'image': 'mark-of-the-holy-sacrian-empire.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Message in a Bottle': {
        'name': 'Message in a Bottle',
        'rarity': 0,
        'image': 'message-in-a-bottle.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Mist-bearing Gourd Bottle': {
        'name': 'Mist-bearing Gourd Bottle',
        'rarity': 0,
        'image': 'mist-bearing-gourd-bottle.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Moguro Mask': {
        'name': 'Moguro Mask',
        'rarity': 0,
        'image': 'moguro-mask.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Nahun\'s Key': {
        'name': 'Nahun\'s Key',
        'rarity': 0,
        'image': 'nahun-s-key.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Nivar\'s Hand': {
        'name': 'Nivar\'s Hand',
        'rarity': 0,
        'image': 'nivar-s-hand.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Oath of Bandits': {
        'name': 'Oath of Bandits',
        'rarity': 0,
        'image': 'oath-of-bandits.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Plague Spores': {
        'name': 'Plague Spores',
        'rarity': 0,
        'image': 'plague-spores.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Poisoned Arrow': {
        'name': 'Poisoned Arrow',
        'rarity': 0,
        'image': 'poisoned-arrow.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Punika Specialty Catalog': {
        'name': 'Punika Specialty Catalog',
        'rarity': 0,
        'image': 'punika-specialty-catalog.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Regulus Statue Fragment': {
        'name': 'Regulus Statue Fragment',
        'rarity': 0,
        'image': 'regulus-statue-fragment.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Solar Salt': {
        'name': 'Solar Salt',
        'rarity': 0,
        'image': 'solar-salt.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Spirit Calling Woodblock': {
        'name': 'Spirit Calling Woodblock',
        'rarity': 0,
        'image': 'spirit-calling-woodblock.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Steel Plate Inscribed with Mysterious Signals': {
        'name': 'Steel Plate Inscribed with Mysterious Signals',
        'rarity': 0,
        'image': 'steel-plate-inscribed-with-mysterious-signals.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'The Epic Tale of Sien': {
        'name': 'The Epic Tale of Sien',
        'rarity': 0,
        'image': 'the-epic-tale-of-sien.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Thirain\'s Wanted Poster': {
        'name': 'Thirain\'s Wanted Poster',
        'rarity': 0,
        'image': 'thirain-s-wanted-poster.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Unsent Letter': {
        'name': 'Unsent Letter',
        'rarity': 0,
        'image': 'unsent-letter.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
    'Voice Breaking the Day': {
        'name': 'Voice Breaking the Day',
        'rarity': 0,
        'image': 'voice-breaking-the-day.webp',
        'category': 'Adventurer\'s Tome',
        'subcategory': None,
        'amount': 1
    },
}


def filter_market_item_name(raw_name: str) -> str | None:
    match = get_close_matches(raw_name, market_map.keys())
    if(len(match) == 0):
        return None
    return match[0]


def get_market_item_by_name(name: str) -> dict:
    return market_map[name]
