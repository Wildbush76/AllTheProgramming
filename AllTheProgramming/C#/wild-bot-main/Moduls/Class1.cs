using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.Commands;
using Discord.WebSocket;
using System.Threading;
using System.IO.Ports;
using System.Speech.Synthesis;
namespace Wild_bot.Moduls
{
    public class Class1 : ModuleBase<SocketCommandContext>
    {
        SpeechSynthesizer ss = new SpeechSynthesizer();
        static SerialPort _serialPort;
        [Command("move")]
        public async Task Move(int xx)
        {

            string aa = Convert.ToString(xx);
            _serialPort = new SerialPort();



            _serialPort.BaudRate = 9600;
            _serialPort.PortName = "COM6";
            _serialPort.Open();

            _serialPort.Write(aa);
            await ReplyAsync("moved!");
            _serialPort.Close();
            Console.WriteLine("moved:" + xx);
        }
        [Command("speak")]
        public async Task say([Remainder]string a=null)
        {
          
            ss.Volume = 100;
            if (a != null)
            {
               ss.Speak(a);
                await ReplyAsync("i has spoken");
            }
            else {
                await ReplyAsync("error 404 message not found");
            }
        }
       
        [Command("help")]
        public async Task Help()
        {
           await ReplyAsync("My commands are ?monkey, ?baby, ?gnir lleb, ?ban, ?Wildbush, ?unban, ?iq, ?Shutdown, ?y or n, ?russian roulette and ?help");

        }

        [Command("monkey")]
        public async Task monkey()
        {
           await monk();

        }
        public async Task monk()
        {
            Random rand = new Random();
            int mon = rand.Next(1, 12);
            Console.WriteLine("Monkey:" + Context.User.Username + ":time:" + Context.Message.Timestamp + ":monkey:" + mon);
            switch (mon)
            {
                case 1:
                    await ReplyAsync("https://tenor.com/view/gog-gog-monkey-gog12-gog-meme-gunna-monkey-gif-18733043");
                    break;
                case 2:
                    await ReplyAsync("https://tenor.com/view/gorila-gorilla-falling-monkey-caiu-gif-18030879");
                    break;
                case 3:
                    await ReplyAsync("https://tenor.com/view/fat-eating-monkey-fast-hungry-gif-15734457");
                    break;
                case 4:
                    await ReplyAsync("https://tenor.com/view/louis-fat-lol-monkey-eat-gif-17851259");
                    break;
                case 5:
                    await ReplyAsync("https://tenor.com/view/spin-monkey-silly-gif-17395248");
                    break;
                case 6:
                    await ReplyAsync("https://tenor.com/view/gorilla-walking-run-gif-14877257");
                    break;
                case 7:
                    await ReplyAsync("https://tenor.com/view/obese-monkey-fat-monkey-summer-belly-eating-lettuce-summer-look-gif-13014350");
                    break;
                case 8:
                    await ReplyAsync("https://tenor.com/view/baked-munchies-caught-gorilla-jungle-gif-5471439");
                    break;
                case 9:
                    await ReplyAsync("https://tenor.com/view/gorila-ass-culo-de-gorilla-monkey-rascar-culo-gif-15809484");
                    break;
                case 10:
                    await ReplyAsync("https://tenor.com/view/gibbon-monkey-indonesia-nature-trees-gif-3440358");
                    break;
                case 11:
                    await ReplyAsync("https://tenor.com/view/banana-monkey-silly-fat-monkey-monkey-crazy-gif-18647865");
                    break;
                    



            }
           

        }
        
        [Command("russian roulette")]
        public async Task rr()
        {
            var rr = new Random();
            var luck = rr.Next(0, 7);
            Console.WriteLine(luck);
            if (luck == 4)
            {
                await Context.Guild.AddBanAsync(Context.User, 0, "not a lucky man");
                await ReplyAsync("*BANG* out of luck");
            }
            else {
                await ReplyAsync("*click* you get to live another day");
            }
        }
        [Command("ban")]
        public async Task Ban(IGuildUser user = null, [Remainder] string reason = null)
        {
            Console.WriteLine("Ban:" + Context.User.Username + ":time:" + Context.Message.Timestamp + ":Banned:" + user);
            if (Context.User.Username.Contains("wildbush"))
            {

                if (user == null)
                {
                    await ReplyAsync("needs a user");

                }
                else if (reason == null)
                {
                    await ReplyAsync("needs a reason");
                }

                else
                {

                    await Context.Guild.AddBanAsync(user, 0, reason);
                    var em = new EmbedBuilder()
                        .WithTitle("haha get banned by " + Context.User.Username)
                        .WithColor(Discord.Color.Red)
                        .WithDescription($":white_check_mark: {user.Mention} was banned **reason**\n{reason}");
                    Embed embed = em.Build();
                    await ReplyAsync(embed: embed);

                }
            }
            else
            {
                await ReplyAsync("only wildbush can use this");
            }
        }
        [Command("Wildbush")]
        
        public async Task wild()
        {
           
            var em = new EmbedBuilder()
                .WithTitle("WildBush")
                .WithDescription($":white_check_mark: Wildbush is a god, we all wish to be more like him. He has done no wrong, He also possses power comparable to gods. - Wildbush \n (those who oppose him shall perish)");

            Console.WriteLine("Wildbush:" + Context.User.Username + ":time:" + Context.Message.Timestamp);
            Embed embed = em.Build();
            await ReplyAsync(embed: embed);

        }

        
        
       
        [Command("henry")]
        public async Task henry()
        {
            var em = new EmbedBuilder()
               .WithTitle("Henry")
               .WithImageUrl("https://cdn.discordapp.com/attachments/777895965171646484/777931076017586176/image0.gif")
               .WithDescription("Epic Boi");
            Console.WriteLine("Henry:" + Context.User.Username + ":time:" + Context.Message.Timestamp);

            Embed embed = em.Build();
            await ReplyAsync(embed: embed);
            


        }
  
        
        [Command("iq")]
        public async Task iq( [Remainder]string other = null)
        {
            
            Random rand = new Random();
            int b = rand.Next(0 , 300);
            Console.WriteLine("IQ:" + Context.User.Username + ":time:" + Context.Message.Timestamp + ":iq:" + b);
            
            if (other == null)
            {
                await ReplyAsync("Your IQ is " + b); 
            }
            else
            {
                await ReplyAsync("seems like " + other + " has a IQ of " + b);
            }

        }

       
        [Command("shutdown")]
public async Task down(string pass = null)
        {
            Console.WriteLine("ShutDown:" + Context.User.Username + ":time:" + Context.Message.Timestamp + ":code:" + pass);
            if (pass == null)
            {
                await ReplyAsync("Requires code");
            }
            else if(pass == "2342")
            {
               await Context.Message.DeleteAsync();
                await ReplyAsync("bot shutting down");
                Environment.Exit(1);
            }
            else
                    {
                await ReplyAsync("incorrect code");
            }

        }
        [Command("y or n")]
        public async Task yes([Remainder]string ques = null)
        {
            Random rand = new Random();
            int f = rand.Next(1 , 12);
            string mes = "";
            Console.WriteLine("Y or N:" + Context.User.Username + ":time:" + Context.Message.Timestamp + ":answer:" + f);
            if (ques == null)
            {
                await ReplyAsync("please add a message");
             return;

            }
            switch(f)
            { 
                case 1:
                    mes = "nope";

                    break;
                case 2:
                    mes = "yes";
                    break;
                case 3:
                    mes = "yep";
                    break;
                case 4:
                    mes = "NO";
                    break;
                case 5:
                    mes = "100% a yes";
                    break;
                case 6:
                    mes = "100% a NO";
                    break;
                case 7:
                    mes = "Y E S";
                    break;
                case 8:
                    mes = "YESSSSSSSSSSSSSSSS";
                    break;
                case 9:
                    mes = "Thats a no";
                    break;
                case 10:
                    mes = "ofc";
                    break;
                case 11:
                    mes = "NO, thats no";
                    break;
                case 12:
                    mes = "most likly a yes";
                    break;
                case 13:
                    mes = "oh thats a yes";
                    break;
            }
            await ReplyAsync(mes);

        }


    }

}

