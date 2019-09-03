/**
* THIS PAYPAL EMAIL VALIDATOR 
* CLASS WAS BUILT BY FU
* DIPERLARANGKAN MENJUAL SIMPLE BASED ! INPUT TXT ? ,berusaha udh gw freein kontol
* ON 3 September
* CopyRight 2019
* Developed Eric Pedra 
* Thanks Fu
*/
var request = require('request'); // npm install requests --save
var readl = require('readline');  // npm install readline --save
var bacaf = require('fs');


  
  // ---------- banner ----------
console.log(`
  PayPal Validator V1.1 (Node Javascript BASED CLI) 
  node paypal.js
  npm install requests --save , npm install readline --save
  Input Email                                                         
  Thanks to : Eric Pedra, Fu 
  is this free ! 
`);
  // ---------- quest ----------
  const tanya = readl.createInterface({
    input : process.stdin,
    output: process.stdout
  }); tanya.question('Masukan Email : ', (kotol) => {
      tanya.close();

// Malu Api kontol , Saya Berharap Muka Lu Kaya Ikan Paisx
request(`http://railwaylinks.com/PayPal-checker/PayPal-checker/api.php?email=${kotol}`, function(error, response, body){
    data = JSON.parse(body)
    console.log(" -------- Hasil -------- ");
    if (data["error_code"] === 209){
        console.log(' [×] DEAD KONTOL  !')
    }else if(data["error_code"] === 0){
        console.log(' [√] LIVE KONTOL')
    }
}); });
// ---------- done ----------