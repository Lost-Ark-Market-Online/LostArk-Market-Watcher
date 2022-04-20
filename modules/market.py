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
}


def get_market_item_by_name(name):
    match = get_close_matches(name, market_map.keys())
    if(len(match) == 0):
        return None
    return market_map[match[0]]
