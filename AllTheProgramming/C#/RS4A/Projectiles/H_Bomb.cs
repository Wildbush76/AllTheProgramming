using System;
using Microsoft.Xna.Framework;
using Terraria;
using Terraria.Audio;
using Terraria.ID;
using Terraria.ModLoader;
using RS4A.Tiles;
namespace RS4A.Projectiles
{
	public class H_Bomb : ModProjectile
	{
		public override void SetStaticDefaults()
		{

			DisplayName.SetDefault("Nuke");

		}
		public override void SetDefaults()
		{
			Projectile.damage = 500;
			Projectile.friendly = false;
			Projectile.DamageType = DamageClass.Ranged;
			Projectile.width = 8;
			Projectile.height = 8;
			Projectile.aiStyle = 16;
			Projectile.penetrate = 1;
			Projectile.timeLeft = 180;
		}
		public override void Kill(int timeLeft)
		{

			bool f = false;
			Vector2 position = Projectile.Center;
			SoundEngine.PlaySound(SoundID.Item14, position);
			Random crat = new Random();
			int radius = 150;
			for (int k = 0; k < 2; k++)
			{
				for (int x = -radius; x <= radius; x++)
				{
					for (int y = -radius; y <= radius; y++)
					{
						int xPosition = (int)(x + position.X / 16.0f);
						int yPosition = (int)(y + position.Y / 16.0f);

						if (Math.Sqrt(x * x + y * y) <= radius + 0.5)
						{
							if (f == true && Framing.GetTileSafely(xPosition, yPosition).HasTile)
							{
								int xadd = crat.Next(1,7);
								int yadd = crat.Next(1,7);
								int xsub = crat.Next(1, 7);
								int ysub = crat.Next(1, 7);
								int fill = crat.Next(1, 11);
								if(yadd < 5)
                                {
									yPosition++;
                                }
								if (xadd  < 5)
								{
									xPosition++;
								}
								if(xsub < 5)
                                {
									xPosition--;
                                }
								if(ysub < 5)
                                {
									yPosition--;
                                }
								if(fill < 9)
							        {
									WorldGen.KillTile(xPosition, yPosition, false, false, false);
								}  
									WorldGen.PlaceTile(xPosition, yPosition, ModContent.TileType<Radstone>(), true);
								

							}
							if (f == false)
							{
								WorldGen.KillTile(xPosition, yPosition, false, false, false);
								Dust.NewDust(position, 22, 22, DustID.Smoke, 0.0f, 0.0f, 120, new Color(), 1f);
							}
						}
					}
				}
				f = true;
				radius += 5;
			}

		}



	}
}
