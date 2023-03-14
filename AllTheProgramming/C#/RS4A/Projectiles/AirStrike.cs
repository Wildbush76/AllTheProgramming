﻿using System;
using Microsoft.Xna.Framework;

using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
namespace RS4A.Projectiles
{
	public class AirStrike : ModProjectile
	{
		public override void SetStaticDefaults()
		{

			DisplayName.SetDefault("AirStrike");

		}
		public override void SetDefaults()
		{
			Projectile.damage = 10;
			Projectile.friendly = true;
			Projectile.DamageType = DamageClass.Ranged;
			Projectile.width = 10;
			Projectile.height = 10;
			Projectile.aiStyle = ProjectileID.Flare;
			Projectile.penetrate = 2;
			Projectile.timeLeft = 400;
		
		
		}

        public override void Kill(int timeLeft)
        {
			Random ran = new Random();
			for (int x = 0; x < ran.Next(10, 40); x++)
			{
				//Projectile.NewProjectile(Projectile.getRect(), new Vector2(ran.Next(-10,10), ran.Next(-1,1)), ProjectileID.Dy, 0, 0,1,16);
				//screw this
			}
        }





    }
}
