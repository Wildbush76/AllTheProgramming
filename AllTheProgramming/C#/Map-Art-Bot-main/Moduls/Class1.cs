using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.Commands;
using Discord.WebSocket;
using System.Threading;
using System.Linq;
namespace Wild_bot.Moduls
{
    public class Class1 : ModuleBase<SocketCommandContext>
    {
             [Command("help")]
        public async Task Help()
        {
           await ReplyAsync("Help yourself. (or ask wildbush)");
            
        }
       
       
        [Command("scoreboard")]
        public async Task scoreboard()
        {
            ITextChannel idk = Context.Client.GetChannel(863517738705879076) as ITextChannel;
            var messia = await idk.GetMessagesAsync(100).FlattenAsync();
            IMessage[] mess = messia.ToArray();
            //int step = 0;
            //string[] people = new string[50];
            //int[] count = new int[50];
            List<string> people = new List<string>();
            List<int> count = new List<int>();


            for (int k = 0; k < mess.Length; k++)
            {
                char[] separators = new char[] { ' ', '\n', ':', ',', '&' };
                string[] broke = mess[k].ToString().Split(separators, StringSplitOptions.RemoveEmptyEntries);

                bool start = false;
                for (int kk = 0; kk < broke.Length; kk++)
                {

                    if (broke[kk] == "and")
                    {
                        continue;
                    }
                    if (start == true)
                    {

                        if (!people.Contains(broke[kk], StringComparer.OrdinalIgnoreCase))
                        {
                            people.Add(broke[kk]);
                            count.Add(1);

                        }
                        else
                        {
                            int a  = people.FindIndex(x => x.Equals(broke[kk],StringComparison.OrdinalIgnoreCase));
                            count[a]++;

                        }
                        if (broke[kk + 1].ToLower().Contains("date") || broke[kk + 1].ToLower().Contains("("))
                        {
                            break;
                        }


                    }
                    if (broke[kk].ToLower().Contains("artist"))
                    {
                        start = true;

                    }
                }
            }


            List<(string A, int B)> art = new List<(string, int)>();


            for (int jeff = 0; jeff < 15; jeff++)
            {
                if (people.Count <= jeff)
                {
                    break;
                }
                art.Add((people[jeff], count[jeff]));
            }

            var test = art.OrderByDescending(Tuple => Tuple.Item2).Select(x => $"{x.A} : {x.B}");

            var em = new EmbedBuilder()
                        .WithTitle("ScoreBoard")
                        .WithColor(Color.Green)
                        .WithDescription(string.Join("\n", test));

            Embed embed = em.Build();
            await ReplyAsync(embed: embed);
        }
        [Command("map")]
        public async Task Map(string person = null)
        {
            Console.WriteLine("map" + Context.User.Username + ":time:" + Context.Message.Timestamp );
           
            if (Context.Channel.Id.ToString() == "875438285873360936")
            {

                ITextChannel chan = Context.Client.GetChannel(863517738705879076) as ITextChannel;

                var mess = await chan.GetMessagesAsync(99).FlattenAsync();
                if (person == null)
                {
                    Random ran = new Random();
                    int k = ran.Next(0, mess.ToArray().Length);
                    var em = new EmbedBuilder()
                        .WithTitle("Map Art")
                        .WithImageUrl(mess.ToArray()[k].Attachments.First().Url)
                        .WithColor(Color.Green)
                        .WithDescription(mess.ToArray()[k].ToString());

                    Embed embed = em.Build();
                    if (!mess.ToArray()[k].ToString().ToLower().Contains("tassos369") && !mess.ToArray()[k].ToString().ToLower().Contains("anonymous"))
                    {
                    await ReplyAsync(embed: embed);
                }
                }
                else
                {
                    person = person.ToLower();
                    IMessage[] sushi = mess.ToArray();
                    IMessage[] end = new IMessage[sushi.Length];
                    int b = 0;
                    for(int r = 0; r < sushi.Length; r++)
                    {
                        if(sushi[r].ToString().ToLower().Contains(person))
                        {
                            end[b] = sushi[r];
                            b++;
                        }
                    }
                    if(end[0] == null)
                    {
                        Console.WriteLine("User hasnt made a map");
                        await ReplyAsync("Specifed user has not made a map");
                    } 
                    else
                    {
                        Random ran = new Random();
                        int k = ran.Next(0, b);
                        var em = new EmbedBuilder()
                            .WithTitle("Map Art")
                            .WithImageUrl(end[k].Attachments.First().Url)
                            .WithColor(Color.Green)
                            .WithDescription(end[k].ToString());

                        Embed embed = em.Build();
                        if (!end[k].ToString().ToLower().Contains("tassos369") && !end[k].ToString().ToLower().Contains("anonympus"))
                    {
                        await ReplyAsync(embed: embed);
                    }
                    }

                }
            }
        }
        
       [Command("Lmap")]
        public async Task LMap(string person = null)
        {
            
           Console.WriteLine("Lmap" + Context.User.Username + ":time:" + Context.Message.Timestamp );
            if (Context.Channel.Id.ToString() == "875438285873360936")
            {

                ITextChannel chan = Context.Client.GetChannel(754664165574049864) as ITextChannel;

                var mess = await chan.GetMessagesAsync(250).FlattenAsync();
                if (person == null)
                {
                    Random ran = new Random();
                    int k = ran.Next(0, mess.ToArray().Length);
                    var em = new EmbedBuilder()
                        .WithTitle("Map Art")
                        .WithImageUrl(mess.ToArray()[k].Attachments.First().Url)
                        .WithColor(Color.Green)
                        .WithDescription(mess.ToArray()[k].ToString());

                    Embed embed = em.Build();
                    if (!mess.ToArray()[k].ToString().ToLower().Contains("tassos369"))
                    {
                    await ReplyAsync(embed: embed);
                }
                }
                else
                {
                    person = person.ToLower();
                    IMessage[] sushi = mess.ToArray();
                    IMessage[] end = new IMessage[sushi.Length];
                    int b = 0;
                    for(int r = 0; r < sushi.Length; r++)
                    {
                        if(sushi[r].ToString().ToLower().Contains(person))
                        {
                            end[b] = sushi[r];
                            b++;
                        }
                    }
                    if(end[0] == null)
                    {
                        Console.WriteLine("User hasnt made a map");
                        await ReplyAsync("Specifed user has not made a map");
                    } 
                    else
                    {
                        Random ran = new Random();
                        int k = ran.Next(0, b);
                        var em = new EmbedBuilder()
                            .WithTitle("Map Art")
                            .WithImageUrl(end[k].Attachments.First().Url)
                            .WithColor(Color.Green)
                            .WithDescription(end[k].ToString());

                        Embed embed = em.Build();
                        if (!end[k].ToString().ToLower().Contains("tassos369"))
                    {
                        await ReplyAsync(embed: embed);
                    }
                    }

                }
            }
        }
        
       
    }

}

