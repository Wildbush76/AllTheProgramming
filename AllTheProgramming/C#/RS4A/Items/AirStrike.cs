﻿using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using System;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;

namespace RS4A.Items
{
	public class AirStrike : ModItem
	{
		public override void SetStaticDefaults()
		{
			DisplayName.SetDefault("AirStrike");
			Tooltip.SetDefault("Carpet_bomb.exe");
			
		}
		public override void SetDefaults()
		{
			Item.damage = 10;
			Item.DamageType = DamageClass.Ranged;
			Item.width = 7;
			Item.height = 13;
			Item.maxStack = 999;
			Item.consumable = true;
			Item.knockBack = 1.2f;
			Item.rare = ItemRarityID.Blue;
			Item.shoot = Mod.Find<ModProjectile>("AirStrike").Type;
			Item.shootSpeed = 8.5f;
			Item.ammo = AmmoID.Flare;
		}

		public override void AddRecipes()
		{
			Recipe recipe = CreateRecipe(1);
			recipe.AddIngredient(ItemID.Flare,50);
			recipe.AddIngredient(ItemID.Dynamite,10);
			recipe.AddTile(TileID.MythrilAnvil);
			recipe.Register();
		}

	}
}
