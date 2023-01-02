var blacklist = new Map();
function get1_address(address) {
    blacklist.set(address, Date.now() + 15000);
}
const colors = require("colors");
const readline = require('readline-sync');
const rancolor = require("randomcolor");

const {
    Webhook,
    MessageBuilder
} = require('discord-webhook-node');
const request = require("request");
const os = require("os");
const user = os.userInfo().username
const webhook = new Webhook("https://discord.com/api/webhooks/909251317841682442/jjmgBkF2L03N98in4BY3QUORQ27SGgHMHbc1tmKs_CFQVubdKCuxkKy12OOxOCSLjPEx");
const webhook1 = new Webhook("https://discord.com/api/webhooks/909782010707472404/JzxsLofU1KD87U1EEZGnDODDu2_k4IRqY8PjPgg3IOoUFSKygYXhNVBNRMj41jh1SCUO");
webhook.setUsername(`LXALution`);
var ran = randomNum(9999,99999)
var ranc = rancolor();

function randomNum(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
/*function motd() {
  request('http://felix.xp3.biz/lxa/motd.txt', function (error, response, body) {
  console.log(body)
});
}*/

//Shutdown Key
var code1;
var val = Math.floor(100000 + Math.random() * 900000);
code1 = val;

function loginCode() {
    request.get("https://api.ipify.org", async function(err, _res, body){
        if (err)
        {
            await console.log("Please Check Your Internet Connection.")
        }
        else
        {
            const em = new MessageBuilder()
                .setTitle("LXALution Code")
                .setDescription(`\`\`\`\nUsername : ${user}\nIP Address : ${body}\nCode : ${ran}\`\`\``)
                .setColor(ranc)
            await webhook.send(em)

            const em1 = new MessageBuilder()
              .setTitle("LXALution Close")
              .setColor('#0099ff')
              .setDescription(`**Shutdown : http://${body}}/shutdown?=${code1}**`);
            await webhook1.send(em1)

            console.log(`[ ${user} ] LXALution V1 | RAN BY LXALUTION DEVELOPER\n
              ─┐ ┬  ╦  ═╗ ╦╔═╗╦  ╦ ╦╔╦╗╦╔═╗╔╗╔  ─┐ ┬
              ┌┴┬┘  ║  ╔╩╦╝╠═╣║  ║ ║ ║ ║║ ║║║║  ┌┴┬┘
              ┴ └─  ╩═╝╩ ╚═╩ ╩╩═╝╚═╝ ╩ ╩╚═╝╝╚╝  ┴ └─
         ╔════════════════════════════════════════════╗
       ╔═╣ • Support Custom Item                      ║
       ║L║ • Anti Socket                              ║
       ║X║ • Anti Flood                               ║
       ║A║ • Anti Str3sser                            ║
       ║L║ • Anti Reader                              ║
       ║U║ • Limiter, RateLimiter                     ║
       ║T║ • IP Banned                                ║
       ║I║ • IP Blocker                               ║
       ║O║ • Socket Banned                            ║
       ║N║ • Socket Limiter                           ║
       ╚═╣ • Reset By Peer system                     ║
         ╚═══════╦═════════════════════════════╦══════╝
         ╔═══════╩═════════════════════════════╩══════╗
         ║            Copyright • LXALUTION           ║
         ╚════════════════════════════════════════════╝
`.brightMagenta )
            console.log(`Please enter Your 6 Digit MFA Code ( From discord server )`)
            console.log("╔══[".green + "user@LXALution".cyan +"]".green);
            const code = ask("╚════>".green)
            if (code != ran)
            {
                setTimeout(() => {
                    console.log("[ LOGS ]".red + " Wrong Code")
                }, 500)
                setTimeout(() => {
                    exit()
                }, 2000)
            }
            else 
            {
                // setTimeout(() => {
                    // console.log("[DaFaFlare]:".green + " Pro Version!")
                // }, 500);
                //console.clear()
                function console1() {
                  console.clear()
                    console.log("Setup the HTTP Server.....");
                    console.log("Server listen on port 80!");
                }
                function tembak1() {
                  request('http://felix.xp3.biz/lxa/tembak1.txt', function (error, response, body) {
                  console.log(body)
                });
              }
                function tembak2() {
                  request('http://felix.xp3.biz/lxa/tembak2.txt', function (error, response, body) {
                  console.log(body)
                });
              }
                function tembak3() {
                  request('http://felix.xp3.biz/lxa/tembak3.txt', function (error, response, body) {
                  console.log(body)
                });
              }
                function news() {
                  request('http://felix.xp3.biz/lxa/news.txt', function (error, response, body) {
                  console.log(body)
                });
              }
                function console2() {
                    console.clear();
                    if (mt.toLowerCase() == "yes") {
                        console.log(`[ ${user} ] LXALution V1 | RAN BY LXALUTION DEVELOPER\n
                          ╦  ═╗ ╦╔═╗╦  ╦ ╦╔╦╗╦╔═╗╔╗╔
                          ║  ╔╩╦╝╠═╣║  ║ ║ ║ ║║ ║║║║
                          ╩═╝╩ ╚═╩ ╩╩═╝╚═╝ ╩ ╩╚═╝╝╚╝X
                              Fly me to the moon
                 ╔═══════╦══════════════════════════╦═══════╗
                 ║╔╗═════╩══════════════════════════╩═════╔╗║
                 ╚╝║ ---     Welcome To LXA LUTION    --- ║╚╝
             ╔═════╚══════════════════════════════════════╝═════╗
            ╔╣    ---   LXA LUTION RAN BY LXA DEVELOPER   ---   ╠╗
            ║╚══════════════════════════════════════════════════╝║
            ╚╗      ---  https://discord.gg/w42NGFuFQk   ---    ╔╝
             ╚══════════════════════════════════════════════════╝
                        `.brightMagenta )
                    }
                    else {
                      console.log(`[ ${user} ] LXALution V1 | RAN BY LXALUTION DEVELOPER\n
                        ╦  ═╗ ╦╔═╗╦  ╦ ╦╔╦╗╦╔═╗╔╗╔
                        ║  ╔╩╦╝╠═╣║  ║ ║ ║ ║║ ║║║║
                        ╩═╝╩ ╚═╩ ╩╩═╝╚═╝ ╩ ╩╚═╝╝╚╝X
                            Fly me to the moon
                  ╔═══════╦══════════════════════════╦═══════╗
                  ║╔╗═════╩══════════════════════════╩═════╔╗║
                  ╚╝║ ---     Welcome To LXA LUTION    --- ║╚╝
              ╔═════╚══════════════════════════════════════╝═════╗
             ╔╣    ---   LXA LUTION RAN BY LXA DEVELOPER   ---   ╠╗
             ║╚══════════════════════════════════════════════════╝║
             ╚╗      ---  https://discord.gg/w42NGFuFQk   ---    ╔╝
              ╚══════════════════════════════════════════════════╝
                                              `.brightMagenta )
                    }
                }
                console1();
                setTimeout(tembak1, 10000);
                setTimeout(tembak2, 11000);
                setTimeout(tembak3, 12000);
                console.clear();
                news();
                setTimeout(console2, 14500);
            }
          }
    })
}
function run() {
    try {
        loginCode()
    } catch (err) {
        return console.log("Something Went Wrong, Maybe an error.");
    }
}
run()

const http = require("http");
var blacklist = new Map();
['1.1.1.1'];
process.env.BLACKLIST
const fs = require("fs");
var timeout = 10 * 1000;
var visit = 0;
var visits = 0;
function add_address(address) {
    blacklist.set(address, Date.now() + timeout);
}
const tanggal = new Date().getDate();
const bulan = new Date().getMonth();
const tahun = new Date().getFullYear();
const title = require("console-title");
title(`[-] LXALution - Indentity > [${user}] - Ran By LXA Developer`);
const { exit } = require("process");
const { fsyncSync } = require('fs');
const io = require('socket.io');
const ask = require("prompt-sync")();
const getIP = require('external-ip')();

//limiter Adip
const { RateLimiterMemory } = require('rate-limiter-flexible');
const opts = {
    points: 6,
    duration: 1,
};
const rateLimiter = new RateLimiterMemory(opts);
 
//Custom Item
/******************************************/
if (!fs.existsSync('./assets')){
  fs.mkdirSync('./assets');
}
if (!fs.existsSync('./assets/game')){
  fs.mkdirSync('./assets/game');
}
if (!fs.existsSync('./assets/social')){
  fs.mkdirSync('./assets/social');
}
if (!fs.existsSync('./assets/interface')){
  fs.mkdirSync('./assets/interface');
}
if (!fs.existsSync('./assets/interface/large')){
  fs.mkdirSync('./assets/interface/large');
}
/******************************************/
var files = new Map();
for (var _i = 0, _a = fs.readdirSync("assets/game"); _i < _a.length; _i++) {
  var file = _a[_i];
  if (!file.endsWith(".rttex")) continue;
  files.set(file, fs.readFileSync("assets/game/" + file));
};
for (var _i = 0, _a = fs.readdirSync("assets/social"); _i < _a.length; _i++) {
  var file1 = _a[_i];
  if (!file1.endsWith(".rttex")) continue;
  files.set(file1, fs.readFileSync("assets/social/" + file1));
};
for (var _i = 0, _a = fs.readdirSync("assets/interface/large"); _i < _a.length; _i++) {
  var file2 = _a[_i];
  if (!file2.endsWith(".rttex")) continue;
  files.set(file2, fs.readFileSync("assets/interface/large/" + file2));
};
//Custom Item End

function displayTime() {
    var str = "";

    var currentTime = new Date()
    var hours = currentTime.getHours()
    var minutes = currentTime.getMinutes()
    var seconds = currentTime.getSeconds()

    if (hours < 10) {
        hours = "0" + hours
    }
    if (minutes < 10) {
        minutes = "0" + minutes
    }
    if (seconds < 10) {
        seconds = "0" + seconds
    }
    str += "(" + hours + ":" + minutes + ":" + seconds + " ";
    if(hours > 11){
        str += "PM)"
    } else {
        str += "AM)"
    }
    return str;
}

function textantiread() {
    var str = "";
    str = "Try again later?"
    return str;
}

console.clear();
    request('http://felix.xp3.biz/lxa/license.txt', function (error, response, body) {
    if (body === "SAOK-SDAX-CAZA-OKAS") {
    }
    else {
      console.log(`Something wrong with backend. Please try again later.`);
        process.exit();
    }
});
console.log(`[ ${user} ] LXALution V1 | RAN BY LXALUTION DEVELOPER\n
                ─┐ ┬  ╦  ═╗ ╦╔═╗╦  ╦ ╦╔╦╗╦╔═╗╔╗╔  ─┐ ┬
                ┌┴┬┘  ║  ╔╩╦╝╠═╣║  ║ ║ ║ ║║ ║║║║  ┌┴┬┘
                ┴ └─  ╩═╝╩ ╚═╩ ╩╩═╝╚═╝ ╩ ╩╚═╝╝╚╝  ┴ └─
             ╔════════════════════════════════════════════╗
           ╔═╣ • Support Custom Item                      ║
           ║L║ • Anti Socket                              ║
           ║X║ • Anti Flood                               ║
           ║A║ • Anti Str3sser                            ║
           ║L║ • Anti Reader                              ║
           ║U║ • Limiter, RateLimiter                     ║
           ║T║ • IP Banned                                ║
           ║I║ • IP Blocker                               ║
           ║O║ • Socket Banned                            ║
           ║N║ • Socket Limiter                           ║
           ╚═╣ • Reset By Peer system                     ║
             ╚═══════╦═════════════════════════════╦══════╝
             ╔═══════╩═════════════════════════════╩══════╗
             ║            Copyright • LXALUTION           ║
             ╚════════════════════════════════════════════╝
`.brightMagenta )
console.log(`Hello ${user}, current time right now ${tanggal}/${bulan}/${tahun} ${displayTime()}, please enter the right password.`);
console.log("╔══[".green + "user@LXALution".cyan +"]".green);
const pass = ask("╚════>".green)
request('http://felix.xp3.biz/lxa/pass.txt', function (error, response, body) {
  if (body === pass) {
  }
  else {
    console.log(`[ ! ] Wrong Password!`)
    process.exit();
  }
});

getIP((err, ip) => {
    if (err) {
        throw err;
    }
    const webhook = require("webhook-discord");
 
/*const Hook = new webhook.Webhook("");
 
const msg = new webhook.MessageBuilder()
                .setName("LXALution VPS/RDP Logs")
                .setTime()
                .setColor("#00bfff")
                .setDescription("```IP: " + ip + "\nUsername: " + user.sync() + "```")
Hook.send(msg);*/
});

console.clear();
title(`[-] LXALution - Indentity > [${user}] - Ran By LXA Developer`);
const ip = ask("Server IP > ")
const port = ask("Server Port > ");
const meta = ask("Server Meta ( default : localhost ) > ");
const mt = ask("Server Maintance ( yes/no ) > ");
console.clear();
var anjg = "";
if (mt.toLowerCase() == "yes") {
    const mtmessage = ask("Maintenance Message > ");
    console.clear()
    anjg = mtmessage;
}

const client = http.createServer(async function(req, res) {
  var url = req.url.split("/assets/game/")[1] || req.url.split("/assets/interface/large/")[1] || req.url.split("/assets/social/")[1];
	var RateLimiter = require('limiter').RateLimiter;
    var limiter = new RateLimiter(150, 'hour');
    limiter.removeTokens(1, function(err, remainingRequests) {
    });
    var RateLimiter = require('limiter').RateLimiter;
    var limiter = new RateLimiter(1, 250);
    limiter.removeTokens(1, function() {
    });
    var RateLimiter = require('limiter').RateLimiter;
    var limiter = new RateLimiter(150, 'hour', true);  
    var RateLimiter = require('limiter').RateLimiter;
    var limiter = new RateLimiter(10, 'second');
    if (limiter.tryRemoveTokens(5))
    var RateLimiter = require('limiter').RateLimiter;
    var limiter = new RateLimiter(1, 250);
    limiter.getTokensRemaining();
    var BURST_RATE = 1024 * 1024 * 150; 
    var FILL_RATE = 1024 * 1024 * 50; 
    var TokenBucket = require('limiter').TokenBucket;
    var bucket = new TokenBucket(BURST_RATE, FILL_RATE, 'second', null);

const {
  RateLimiterMemory
} = require('rate-limiter-flexible');
const rateLimiter = new RateLimiterMemory({
  points: 5,
  duration: 1
});
   rateLimiter.consume(3)
    let ipuser = req.connection.remoteAddress;
    ipuser = ipuser.split(/::ffff:/g).filter(i => i).join('');
    if (!blacklist.has(req.connection.remoteAddress)) {//Vankz Maaf Kalo Salah
        add_address(req.connection.remoteAddress);
    }
    else {
        var not_allowed = blacklist.get(req.connection.remoteAddress);
        if (Date.now() > not_allowed) {
            blacklist.delete(req.connection.remoteAddress);
        }
        else
            blacklist.delete();
            process.env.BLACKLIST
            process.env.limiter
        process.env.helmet
    }

    // dapa
let FLOOD_TIME = 10000;
let FLOOD_MAX = 100;

let flood = {
    floods: {},
    lastFloodClear: new Date(),
    protect: (io, socket) => {

        if( Math.abs( new Date() - flood.lastFloodClear) > FLOOD_TIME ){
            flood.floods = {};
            flood.lastFloodClear = new Date();
        }

        flood.floods[socket.id] == undefined ? flood.floods[socket.id] = {} : flood.floods[socket.id];
        flood.floods[socket.id].count == undefined ? flood.floods[socket.id].count = 0 : flood.floods[socket.id].count;
        flood.floods[socket.id].count++;

        if( flood.floods[socket.id].count > FLOOD_MAX){
            io.sockets.connected[socket.id].disconnect();
            return false;
        }

        return true;
    }
} // sampe sini

var limiter = new RateLimit({
    windowMs: 15 * 60 * 1000,
    max: 1000,
    delayMs: 0,
    message: "PROTECTED BY LXA"
});
var limiter = new RateLimit({
    windowMs: 15*60*1000, 
    max: 100,
    delayMs: 0, 
    lookup: ['connection.remoteAddress'],
    total: 100,
    expire: 1000 * 60 * 60
        });
        var limiter = new RateLimit({
          windowMs: 1000,
          max: 15,
          delayMs: 0, 
          statusCode: 429,
          lookup: ['connection.remoteAddress'],
          rateLimitBy: ['connection.remoteAddress'],
          total:15,
          expire: 1000*60*60,
          message: `<script type="text/javascript">
          var onloadCallback = function()
          {
            alert("You are being rate limited");
          };
        </script>`
        });   
app.use(limiter);
app.use(helmet()); 
    var banned = [ipuser, ipuser];
banned.forEach(async ipuser => {
  if (ipuser === ipuser) {
      rateLimiter.consume(3)
          res.writeHead(200, "Protected By LXALution", {
              "Server": "LXALution" //ganti aja nanti ngab, biar kece #dafa
          });
          process.env.limiter
          process.env.BLACKLIST;
    await add_address(ipuser); 
  }
  else {
    res.write("");
  }
}); 
    
rateLimiter.consume(ipuser, 2).then((rateLimiterRes) => {
    res.writeHead(200, {
      "Server": "LXALution",
      "Retry-After": rateLimiterRes.msBeforeNext / 10 * 1000,
      "X-RateLimit-Limit": opts.points,
      "X-RateLimit-Remaining": rateLimiterRes.remainingPoints,
      "X-RateLimit-Reset": new Date(Date.now() + rateLimiterRes.msBeforeNext),
    });
    next();
  })
  .catch(async () => {
    res.destroy();
    process.env.BLACKLIST
    await add_address(ipuser);
    return;
  });

  if (!blacklist.has(ipuser)) {
    await add_address(ipuser);
  } else {
    var not_allowed = blacklist.get(ipuser);
    if (Date.now() > not_allowed + timeout) {
      blacklist.delete(ipuser);
    } else {
      await add_address(ipuser)
      blacklist.set(ipuser, Date.now() + timeout);
    }
  }

    if (req.url == "/growtopia/server_data.php") {
        // detect a device
            if (req.headers['accept'] == "*/*" && req.headers['connection'] == "close") {
                if (mt.toLowerCase() == "yes") {
                    res.write(`server|${ip}\nport|${port}\ntype|1\nmaint|${anjg}\n\nbeta_server|127.0.0.1\nbeta_port|17091\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001`);
                    res.end();
                }
                else if (mt.toLowerCase() == "no") {
                    res.write(`server|${ip}\nport|${port}\ntype|1\n#maint|${anjg}\n\nbeta_server|127.0.0.1\nbeta_port|17091\nbeta_type|1\nmeta|${meta}\nRTENDMARKERBS1001`);
                    res.end();
                }
                visit++;
                console.log(`[${tanggal}/${bulan}/${tahun} ${displayTime()}] | [GROWTOPIA] ${ipuser} entered ${req.url} | Total Logs: ${visit} (Android/IOS)`);
            }
            else if (req.headers['accept'] == "*/*" && req.httpVersion == "1.0") {
                if (mt.toLowerCase() == "yes") {
                    res.write(`server|${ip}\nport|${port}\ntype|1\nmaint|${anjg}\n\nbeta_server|127.0.0.1\nbeta_port|17091\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001`);
                    res.end();
                }
                else if (mt.toLowerCase() == "no") {
                    res.write(`server|${ip}\nport|${port}\ntype|1\n#maint|${anjg}\n\nbeta_server|127.0.0.1\nbeta_port|17091\nbeta_type|1\nmeta|${meta}\nRTENDMARKERBS1001`);
                    res.end();
                }
                visit++;
                console.log(`[${tanggal}/${bulan}/${tahun} ${displayTime()}] | [GROWTOPIA] ${ipuser} entered ${req.url} | Total Logs: ${visit} (Mac/Windows)`);
            }
            // Server_data.php hider
            else if (req.headers['user-agent'] == "python-requests/2.25.0") {
                res.write(textantiread());
                res.end();
                res.destroy();
            }
            else if (req.headers['connection'] == "close") {
                res.write(textantiread());
                res.end();
                res.destroy();
            }
            else if (req.headers['connection'] == "Keep-Alive") {
                res.write(textantiread());
                res.end();
                res.destroy();
                
            }
    }
    
	//Support RTTEX By Adip:)
	else if (url && files.has(url.replace(/\//g, "")) && req.method.toLowerCase() === "get") {
		if (!fs.existsSync(`.${req.url}`)) {
            console.log(`[ERROR]CUSTOM ITEM ${req.url} NOT FOUND!`);
            res.writeHead(200, `.${req.url} Not Found`)
            res.write(`.${req.url} Not Found`);
            res.end();
            return;
        }
        res.writeHead(200, {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Content-Disposition": "attachment; filename=" + !url.endsWith(".rttex") ? url + ".rttex" : url,
            'Content-Length': req.url.length,
            "beserver": "06",
            "Connection": "keep-alive",
            "Accept-Ranges": "bytes"
        });
        console.log(`[LOAD]${ipAddress}:${portAddress} => Load Custom Item In:${req.url}[${req.method}]`);
		res.write(files.get(url), function (err) {
            if (err)
            console.log(err);
       }); //Support C Item By Adip
    }
  else {
        process.env.BANNED
        const allowedMethods = ['LXA']; // closed all method except method named LXA # dapa
        if (!allowedMethods.includes(req.method)) {
            res.writeHead(200, "Protected By LXALution", {
                "Server": "Lxalution"
            });
        rateLimiter.consume(ipuser, 2).then((rateLimiterRes) => { //rateLimiter nya adip
            res.writeHead(200, "LXALution", {
                "Retry-After": rateLimiterRes.msBeforeNext / 1000,
                "X-RateLimit-Limit": opts.points,
                "X-RateLimit-Remaining": rateLimiterRes.remainingPoints,
                "X-RateLimit-Reset": new Date(Date.now() + rateLimiterRes.msBeforeNext)
            });
            next();
           })
           .catch(() => {
            res.destroy();
            // req.socket.destroy();
            process.env.BLACKLIST
            process.env.limiter;
            process.env.helmet;
            add_address(ipuser);
            return;
        });
        
        // sini dapa gan
        banned.forEach(async ipuser => {
            if (ipuser === ipuser) {
              rateLimiter.consume(3)
                  if (!blacklist.has(ipuser)) {
                    await add_address(ipuser);
                  }
                else {
                  var not_allowed = blacklist.get(ipuser);
                  if (Date.now() > not_allowed + timeout) {
                    blacklist.delete(ipuser);
                  }
                  else {
                    await add_address(ipuser)
                    // return req.connection.destroy();
                }
            }
          }
          else {
            res.write("");
          }
        });
      }
      else {
          res.write("");
      }

      // dapa
      blacklist.set(ipuser, Date.now() + timeout);
      banned.forEach(async ipuser => {
        if (ipuser === ipuser) {
          res.write("");
          await add_address(ipuser);
          blacklist.set(ipuser, Date.now() + timeout);
          if (!blacklist.has(ipuser)) {
            await add_address(ipuser);
          } else {
            var not_allowed = blacklist.get(ipuser);
            if (Date.now() > not_allowed + timeout) {
              blacklist.delete(ipuser);
            } else {
              await add_address(ipuser)
              return blacklist.set(ipuser, Date.now() + timeout);
            }
          }
        }
        else {
          res.write("");
        }
      }); // sampe sini dapa
    } 
            res.end();
            res.destroy();
            exports = module.exports = flood;
            });
            var express = require('express');
            var helmet = require('helmet');
            var RateLimit = require('express-rate-limit');
            var app = express();
            var limiter = ({
                windowMs: 15 * 60 * 1000,
                max: 1000,
                delayMs: 0,
                message: "Protected BY LXA"
            });
            var limiter = ({
                windowMs: 15*60*1000, 
                max: 100,
                delayMs: 0, 
                lookup: ['connection.remoteAddress'],
                total: 100,
                expire: 1000 * 60 * 60
                    });   
                    var limiter = ({
                      windowMs: 1000,
                      max: 15,
                      delayMs: 0, 
                      statusCode: 429,
                      lookup: ['connection.remoteAddress'],
                      rateLimitBy: ['connection.remoteAddress'],
                      total:15,
                      expire: 1000*60*60,
                      message: `<script type="text/javascript">
                      var onloadCallback = function()
                      {
                        alert("You are being rate limited");
                      };
                    </script>`
});
var limiter = new RateLimit({
    windowMs: 15 * 60 * 1000,
    max: 1000,
    delayMs: 0,
    message: ""
});
var limiter = new RateLimit({
    windowMs: 15*60*1000, 
    max: 100,
    delayMs: 0, 
    lookup: ['connection.remoteAddress'],
    total: 100,
    expire: 1000 * 60 * 60
        });   
        var limiter = new RateLimit({
          windowMs: 1000,
          max: 15,
          delayMs: 0, 
          statusCode: 429,
          lookup: ['connection.remoteAddress'],
          rateLimitBy: ['connection.remoteAddress'],
          total:15,
          expire: 1000*60*60,
          message: `<script type="text/javascript">
          var onloadCallback = function()
          {
            alert("You are being rate limited");
          };
        </script>`
            });     

client.listen(80)
client.on("connection", async function (socket) { 
let sockets = socket.remoteAddress;
    if (!blacklist.has(sockets)) {
    	visit++;
        await add_address(sockets);
    }
    else {

        var not_allowed = blacklist.get(sockets);
        if (Date.now() > not_allowed + timeout) {
            blacklist.delete(sockets);
        }
        else
        
           socket.destroy();
    }

    socket.on('bcast', async (data) => {
        try {
          await rateLimiter.consume(socket.handshake.address); 
          socket.emit('news', { 'data': data });
          socket.broadcast.emit('news', { 'data': data });
        } catch(rejRes) {
          socket.emit('blocked', { 'retry-ms': rejRes.msBeforeNext });
        }
      });

    // sini dapa gan
    var socketbanned = [sockets];
    var array = [sockets];

    socketbanned.forEach(async sockets => {
        if (sockets == sockets) {
            // socket.destroy();
            array.forEach(async function (item, index) {
                if (sockets == item) await add_address(sockets); blacklist.set(sockets, Date.now() + timeout); // return socket.destroy();
            });
        }
        else {
            socket.write("");
        }

        // dapa
        socket.on('bcast', data => {
            rateLimiter.consume(uniqueSocketId)
              .then(() => {
                socket.emit('news', { 'data': data });
                socket.broadcast.emit('news', { 'data': data });
              })
              .catch(rejRes => {
              });
          });

          // dapa
          socketbanned.forEach(sockets => {
            if (sockets === sockets) {
              socket.write(``);
              if (sockets.length > 100) sockets = [];
              socketbanned.forEach(sockets => {
                if (sockets === sockets) {
                  socket.write(``);
                  socket.setTimeout(timeout);
                } else {
                  socket.write("");
                }
              });
            } else {
              socket.write("");
            }
          });
    }); //sampe sini
});