using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.Commands;
using Discord.WebSocket;
using System.Threading;
using System.Linq;
using Newtonsoft.Json;
using System.Net.Http;
namespace Wild_bot.Moduls
{
    public class Class1 : ModuleBase<SocketCommandContext>
    {
        [Command("VES")]
        public async Task VES() {
           await ReplyAsync("Current enchange rate of USD to VES is 1 USD =  " + string.Format("{0:#,0.00}", Import("VES")) + " VES");   
        }
        [Command("VND")]
        public async Task VND() {
            await ReplyAsync("Current enchange rate of USD to VND is 1 USD =  " + string.Format("{0:#,0.00}", Import("VND")) + " VND");   
        }
        public class API_Obj
        {
            public string result { get; set; }
            public string documentation { get; set; }
            public string terms_of_use { get; set; }
            public string time_zone { get; set; }
            public string time_last_update { get; set; }
            public string time_next_update { get; set; }
            public ConversionRate conversion_rates { get; set; }
        }

        public class ConversionRate
        {
            public double VES { get; set; }
            public double VND { get; set; }
        }

        static Double Import()
        {
                String URLString = "https://v6.exchangerate-api.com/v6/56397de4f1b88727b15953c6/latest/USD";
                using (var webClient = new System.Net.WebClient())
                {
                    var json = webClient.DownloadString(URLString);
                    API_Obj Test = JsonConvert.DeserializeObject<API_Obj>(json);
                    switch(type) {
                    case "VES":
                        return Test.conversion_rates.VES;
                        break;
                    case "VND":
                        return Test.conversion_rates.VND;
                        break;
                }
                
                }
          
        }
    }
}



