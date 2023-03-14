using RS4A.Buffs;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;

namespace RS4A.Items
{
	public class radiological_stick : ModItem
	{
		public override void SetStaticDefaults() 
		{
			DisplayName.SetDefault("Radiological Stick"); 
			Tooltip.SetDefault("Don't burn yourself.");
		}

		public override void SetDefaults() 
		{
			Item.damage = 2;
			Item.DamageType = DamageClass.Melee/* tModPorter Suggestion: Consider MeleeNoSpeed for no attack speed scaling */;
			Item.scale = 1;
			Item.width = 60;
			Item.height = 60;
			Item.useTime = 34;
			Item.useAnimation = 34;
			Item.useStyle = ItemUseStyleID.Swing;
			Item.knockBack = 3;
			Item.value = 1;
			Item.rare = ItemRarityID.Lime;
			Item.crit = 0;
			Item.UseSound = SoundID.Item1;
			Item.autoReuse = true;
			
		}

		public override void AddRecipes() 
		{
			Recipe recipe = CreateRecipe();
			recipe.AddIngredient(ModContent.ItemType<Uranium_or>(),1);
			recipe.AddIngredient(ItemID.Wood, 5);
			recipe.AddTile(TileID.WorkBenches);
			recipe.Register();
		}
		public override void OnHitNPC(Player player, NPC target, int damage, float knockback, bool crit)
		{
				target.AddBuff(ModContent.BuffType<Rad>(), 180);
		}
	}
}
