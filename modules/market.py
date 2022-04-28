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
}


def filter_market_item_name(raw_name: str) -> str | None:
    match = get_close_matches(raw_name, market_map.keys())
    if(len(match) == 0):
        return None
    return match[0]


def get_market_item_by_name(name: str) -> dict:
    return market_map[name]
