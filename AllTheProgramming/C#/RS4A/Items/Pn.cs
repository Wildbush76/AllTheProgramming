
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;

namespace RS4A.Items
{
    public class Pn : ModItem
    {
        public override void SetStaticDefaults()
        {
            DisplayName.SetDefault("porta-nurse");
            Tooltip.SetDefault("a drinkable nurse");
        }

        public override void SetDefaults()
        {
            Item.width = 14;
            Item.height = 23;
            Item.useStyle = ItemUseStyleID.EatFood;
            Item.useAnimation = 15;
            Item.useTime = 15;
            Item.useTurn = true;
            Item.UseSound = SoundID.Item3;
            Item.maxStack = 1;
            Item.consumable = true;
            Item.rare = ItemRarityID.Red;
            Item.value = Item.buyPrice(gold: 50);
            Item.healLife = 4000;
        }
        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddIngredient(ItemID.LifeCrystal, 3);
            recipe.AddIngredient(ItemID.BottledWater, 1);
            recipe.AddIngredient(ItemID.Star, 10);

            recipe.AddTile(TileID.AlchemyTable);
            recipe.Register();
        }
    }
}
