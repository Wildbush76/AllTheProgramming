using RS4A.Buffs;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;

namespace RS4A.Items
{
	public class leeroy_emblem : ModItem
	{
		public override void SetStaticDefaults() 
		{
			DisplayName.SetDefault("Leeroy Emblem"); // By default, capitalization in classnames will add spaces to the display name. You can customize the display name here by uncommenting this line.
			Tooltip.SetDefault("glass canon.mp4");
		}

		public override void SetDefaults() 
		{
			Item.width = 28;
			Item.height = 28;
			Item.value = 0;
			Item.rare = ItemRarityID.Pink;
			Item.accessory = true;

        }
        public override void UpdateEquip(Player player)
		{
			if (player.statDefense < 100) {
				player.GetDamage(DamageClass.Generic) += (10 - player.statDefense / 10);
			}
		}
		public override void AddRecipes() 
		{
			Recipe recipe = CreateRecipe();
			recipe.AddIngredient(ItemID.WarriorEmblem);
			recipe.AddIngredient(ItemID.SummonerEmblem);
			recipe.AddIngredient(ItemID.RangerEmblem);
			recipe.AddIngredient(ItemID.SorcererEmblem);
			recipe.AddIngredient(ItemID.SoulofFlight, 5);
			recipe.AddIngredient(ItemID.SoulofFright, 5);
			recipe.AddIngredient(ItemID.SoulofLight, 5);
			recipe.AddIngredient(ItemID.SoulofMight, 5);
			recipe.AddIngredient(ItemID.SoulofNight, 5);
			recipe.AddIngredient(ItemID.SoulofSight, 5);
			recipe.AddIngredient(ItemID.LunarBar, 50);
			recipe.AddTile(TileID.MythrilAnvil);
			recipe.Register();
		}
	}
}
