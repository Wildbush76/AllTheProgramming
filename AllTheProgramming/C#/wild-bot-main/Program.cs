using System;
using Discord;
using Discord.Commands;
using Discord.WebSocket;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using System.Reflection;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.IO;
using System.Text;

namespace Wild_bot
{
    class Program
    {
        static void Main(string[] args) => new Program().RunBotAsync().GetAwaiter().GetResult();

        private DiscordSocketClient _client;
        private CommandService _commands;
        private IServiceProvider _services;
        private ICommandContext _context;
        public async Task RunBotAsync()
        {
            _client = new DiscordSocketClient();
            _commands = new CommandService();
            _services = new ServiceCollection()

            .AddSingleton(_client)
            .AddSingleton(_commands)
            .BuildServiceProvider();

            string token = "ITS_THE_TOKEN";
            _client.Log += _client_Log;
            await RegisterCommandsAsync();
            await _client.LoginAsync(TokenType.Bot, token);
            await _client.StartAsync();
            await Task.Delay(-1);
        }

        private Task _client_Log(LogMessage arg)
        {
            Console.WriteLine(arg);
            return Task.CompletedTask;
        }

        public async Task RegisterCommandsAsync()
        {
            _client.MessageReceived += HandleCommandAsync;
            await _commands.AddModulesAsync(Assembly.GetEntryAssembly(), _services);
        }
        
       
        public async Task HandleCommandAsync(SocketMessage arg)
        {
            var message = arg as SocketUserMessage;
            var context = new SocketCommandContext(_client, message);
            if (message.Author.Username == "airstream")
            {

                var emoji12 = new Emoji("🤡");

                await message.AddReactionAsync(emoji12);
            }
            if (message.Content.Contains(":") || message.Content.Contains(";"))
                {
                bool found = false;
                char[] fff = new char[message.Content.Length];
                int testt = message.Content.Length;
               // Console.WriteLine(message.Content.Length);
                using (StringReader sr = new StringReader(message.Content))
                {
                    for (int corvidgay = message.Content.Length; corvidgay > 0; corvidgay--)
                    {
                        sr.Read(fff, 0, 1);
                        
                        StringBuilder sb = new StringBuilder("");
                            using (StringWriter sw = new StringWriter(sb))
                            {
                            sw.Write(fff, 0, 1);
                            string wonka = sb.ToString();
                            
                            if (wonka == ":" || wonka == ";")
                            {
                                found = true;
                            }
                            if (found == true)
                            {
                                if (wonka == "," || wonka == ":" || wonka == "." || wonka == "'" )
                                { }
                                else if (wonka == "c" || wonka == "C" || wonka == "(")
                                {
                                    var emoji1 = new Emoji("🤡");
                                    var emoji2 = new Emoji("😢");
                                    var emoji3 = new Emoji("🐵");


                                    await message.AddReactionAsync(emoji1);
                                    await message.AddReactionAsync(emoji3);
                                    await message.AddReactionAsync(emoji2);
                                    await message.Channel.SendMessageAsync( message.Author.Username + " go ahead and cry about it");
                                    await message.Channel.SendMessageAsync(" https://tenor.com/view/cat-kitty-cope-gif-20110606 "); 
                                }
                              
                                else
                                {
                                  return;
                                }
                            }
                            }
                    }
                }
            }
            if (message.Author.IsBot || message.Author.Username == "Tarraccc") return;
            int argPos = 0;
            if (message.HasStringPrefix("?", ref argPos))//bot prefix
            {
                var result = await _commands.ExecuteAsync(context, argPos, _services);
                if (!result.IsSuccess) Console.WriteLine(result.ErrorReason);
                if (result.Error.Equals(CommandError.UnmetPrecondition)) await message.Channel.SendMessageAsync(result.ErrorReason);
            }

        }

    }
    


}   

