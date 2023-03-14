using System;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;

namespace RS4A.Buffs
{
    public class Lead : ModBuff
    {
        public override void SetStaticDefaults()
        {
            Main.persistentBuff[Type] = true;
            DisplayName.SetDefault("Lead poisoning");
            Description.SetDefault("MMMMMM lead");
            
        }
        public override void Update(Player player, ref int buffIndex)
        {

            player.confused = true;
            player.maxRunSpeed = 10;
            player.autoJump = true;
            player.lifeRegen -= 4;

        }

    }
}
