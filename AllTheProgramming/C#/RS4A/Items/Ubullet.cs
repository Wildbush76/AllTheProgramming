﻿using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using System;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;

namespace RS4A.Items
{
	public class Ubullet : ModItem
	{
		public override void SetStaticDefaults()
		{
			DisplayName.SetDefault("Uranium Bullets");
			
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
			Item.shoot = Mod.Find<ModProjectile>("UrBullet").Type;
			Item.shootSpeed = 8.5f;
			Item.ammo = AmmoID.Bullet;
		}

		public override void AddRecipes()
		{
			Recipe recipe = CreateRecipe(50);
			recipe.AddIngredient(null, "Uranium_bar",1);
			recipe.AddIngredient(ItemID.MusketBall, 50);
			recipe.AddTile(TileID.MythrilAnvil);
			recipe.Register();
		}

	}
}
