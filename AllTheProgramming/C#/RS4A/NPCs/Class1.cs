
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Terraria;
using Terraria.ModLoader;
using Terraria.ID;
using RS4A.Items;
using RS4A.Projectiles;

namespace RS4A.NPCs
{
   public class Npc : GlobalNPC
    {
    static int rng = 0;
		public override void SetupShop(int type, Chest shop, ref int nextSlot)
		{

			if (type == NPCID.WitchDoctor)
			{
				shop.item[nextSlot].SetDefaults(ItemID.Bottle);
				nextSlot++;
				
				shop.item[nextSlot].SetDefaults(ModContent.ItemType<armyPot>());
				shop.item[nextSlot].shopCustomPrice = 80000000; //in copper, of course
				nextSlot++;
			} else if (type == NPCID.SkeletonMerchant)
			{
				shop.item[nextSlot].SetDefaults(ItemID.BoneKey);
				shop.item[nextSlot].shopCustomPrice = 500000; 
				nextSlot++;
			}
				if(type == NPCID.PartyGirl)
                {
					shop.item[nextSlot].SetDefaults(ModContent.ItemType<Tnurse>());
					shop.item[nextSlot].shopCustomPrice = 100;
					nextSlot++;
                }
				
		}
		public override void GetChat(NPC npc, ref string chat)
		{
			
			if (npc.type == NPCID.SkeletonMerchant)
			{
				rng = Main.rand.Next(10);
				if (rng == 0)
				{
					chat = "I did your mother, " + Main.LocalPlayer.name.ToString() + " C:.";
				}
				else if (rng == 1) {
					chat =  Main.LocalPlayer.name.ToString() + " ,Ive been trying to reach you about your cars extended warranty";
				}
			}
		}
		
		public override bool PreChatButtonClicked(NPC npc, bool firstButton)
		{
			if (npc.type == NPCID.SkeletonMerchant && rng == 0)
			{
				return false;
			} else
            {
				return true;
			}
		}
		public override void ModifyHitByProjectile(NPC npc, Projectile projectile, ref int damage, ref float knockback, ref bool crit, ref int hitDirection)
		{
			if (npc.HasBuff(BuffID.Venom) && projectile.type == ModContent.ProjectileType<handT>())
			{
				crit = true;
			}
		}

	}
}
