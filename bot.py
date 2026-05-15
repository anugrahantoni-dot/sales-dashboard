from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8824016580:AAFVdhVokUdIeBvPnpE6uHWYn24ycb6gxAU"

# Kamus kode → detail (isi sendiri sesuai data kamu)
# Format:
# "CODE": {"arti": "Nama Item", "sku": "SKU", "brand": "Brand"}
kode_dict = {
    "MABB14": {"arti": "Mmm After Bite Balm 14Gr", "sku":  "V02502110172", "brand": "Momami"},
"MAW10": {"arti": "Mmm Antibacterial Wipes 10S", "sku":  "136323", "brand": "Momami"},
"MAW30": {"arti": "Mmm Antibacterial Wipes 30", "sku":  "132005", "brand": "Momami"},
"MAW60": {"arti": "Mmm Antibacterial Wipes 60S", "sku":  "136324", "brand": "Momami"},
"MBCO": {"arti": "Mmm Baby Care On The Go Kit", "sku":  "130674", "brand": "Momami"},
"MBDS50": {"arti": "Mmm Bb Disinfectant Spr 50Ml", "sku":  "127793", "brand": "Momami"},
"MBDS350": {"arti": "Mmm Bb Disinfectant Spr350ml", "sku":  "126376", "brand": "Momami"},
"MBAM": {"arti": "Mmm Bdl All Medicated", "sku":  "136728M", "brand": "Momami"},
"MBAWW": {"arti": "Mmm Bdl All Wipes White Bag", "sku":  "136727M", "brand": "Momami"},
"MBSTT2": {"arti": "Mmm Bdl Softie Top To Toe 2Pk", "sku":  "136074", "brand": "Momami"},
"MBGBY": {"arti": "Mmm Bluelight Glss Blue/Yello", "sku":  "126560", "brand": "Momami"},
"MBGPP": {"arti": "Mmm Bluelight Glss Pink/Purpl", "sku":  "126559", "brand": "Momami"},
"MBZGB": {"arti": "Mmm Bluelight Zv+ Glasses Blk", "sku":  "128382", "brand": "Momami"},
"MBZGB2": {"arti": "Mmm Bluelight Zv+ Glasses Blue", "sku":  "128381", "brand": "Momami"},
"MBGZGP": {"arti": "Mmm Bluelight Zv+ Glasses Pink", "sku":  "128380", "brand": "Momami"},
"MBBY200": {"arti": "Mmm Bouncy Baby Lotion 200Ml", "sku":  "126616", "brand": "Momami"},
"MBBY100": {"arti": "Mmm Bouncy Baby Yogurt 100Ml", "sku":  "V01302100033", "brand": "Momami"},
"MBNO10": {"arti": "Mmm Breathy Natural Oil 10Ml", "sku":  "130242", "brand": "Momami"},
"MBBW250": {"arti": "Mmm Bubbly Body Wash 250Ml", "sku":  "126615", "brand": "Momami"},
"MCBB50": {"arti": "Mmm Chubby Bumb Balm 50Gr", "sku":  "126418", "brand": "Momami"},
"MCW": {"arti": "Mmm Citrapella Wipes", "sku":  "121680", "brand": "Momami"},
"MCSP": {"arti": "Mmm Citronella Shield Patch", "sku":  "136755M", "brand": "Momami"},
"MCFC15": {"arti": "Mmm Cutie Facial Cream 15Gr", "sku":  "129286", "brand": "Momami"},
"MCFC50": {"arti": "Mmm Cutie Facial Cream 50Gr", "sku":  "126416", "brand": "Momami"},
"MDCRC25": {"arti": "Mmm Dreamy Clm Rub Cream 25Gr", "sku":  "129287", "brand": "Momami"},
"MDCRC50": {"arti": "Mmm Dreamy Clm Rub Cream 50Gr", "sku":  "126417", "brand": "Momami"},
"MEBKMB": {"arti": "Mmm Easy Breezy Kids Mask Boy", "sku":  "126379", "brand": "Momami"},
"MEBKMG": {"arti": "Mmm Easy Breezy Kids Mask Girl", "sku":  "126380", "brand": "Momami"},
"MEBKMGU": {"arti": "Mmm Easy Breezy Kids Mask Unix", "sku":  "126381", "brand": "Momami"},
"MFSB": {"arti": "Mmm Face Shield Baby", "sku":  "126377", "brand": "Momami"},
"MFSK": {"arti": "Mmm Face Shield Kids", "sku":  "126378", "brand": "Momami"},
"MFAA10": {"arti": "Mmm First Aid Antiseptic 10Ml", "sku":  "132937", "brand": "Momami"},
"MFFW": {"arti": "Mmm Foaming Face Wash 100Ml", "sku":  "V02502110178", "brand": "Momami"},
"MFFW2P": {"arti": "Mmm Foaming Face Wash 2Pk", "sku":  "136923M", "brand": "Momami"},
"MFFW3P": {"arti": "Mmm Foaming Face Wash 3Pk", "sku":  "136924M", "brand": "Momami"},
"MFHBCW5": {"arti": "Mmm Frhead&Bdy Cling Wipes 5S", "sku":  "136751M", "brand": "Momami"},
"MFVC300": {"arti": "Mmm Fruit&Veggie Cleanser300ml", "sku":  "126776", "brand": "Momami"},
"MGTPB": {"arti": "Mmm Giggly Toothpaste Banana", "sku":  "126768", "brand": "Momami"},
"MGTPF": {"arti": "Mmm Giggly Toothpaste F Grape", "sku":  "129350", "brand": "Momami"},
"MGTPNO": {"arti": "Mmm Giggly Toothpaste No Flour", "sku":  "129351", "brand": "Momami"},
"MGFBS": {"arti": "Mmm Glss Fcshld Blue+Sticker", "sku":  "126746", "brand": "Momami"},
"MGFCS": {"arti": "Mmm Glss Fcshld Clear+Sticker", "sku":  "126745", "brand": "Momami"},
"MGFGS": {"arti": "Mmm Glss Fcshld Green+Sticker", "sku":  "126748", "brand": "Momami"},
"MGFPS": {"arti": "Mmm Glss Fcshld Pink+Sticker", "sku":  "126747", "brand": "Momami"},
"MGBC": {"arti": "Mmm Gwp Bottle Christmast 2025", "sku":  "136927M", "brand": "Momami"},
"MHP": {"arti": "Mmm Hampers Protection", "sku":  "128377", "brand": "Momami"},
"MHT": {"arti": "Mmm Hampers Toiletries", "sku":  "128376", "brand": "Momami"},
"MHHW250": {"arti": "Mmm Happy Hair Wash 250Ml", "sku":  "126614", "brand": "Momami"},
"MHSSM80": {"arti": "Mmm Hello Sunshine Sun Mist 80", "sku":  "V01302102725", "brand": "Momami"},
"MHOTGK": {"arti": "Mmm Hygiene On The Go Kit", "sku":  "128920", "brand": "Momami"},
"MIBSS15": {"arti": "Mmm Itsy Bitsy Sun Stick 15Gr", "sku":  "128924", "brand": "Momami"},
"MJHG100": {"arti": "Mmm Jolly Handwash Gel 100Ml", "sku":  "128918", "brand": "Momami"},
"MKBWRV": {"arti": "Mmm Kids Bodywash-Rv250ml", "sku":  "V02502110175", "brand": "Momami"},
"MKBWWA": {"arti": "Mmm Kids Bodywash-Wa250ml", "sku":  "V02502110174", "brand": "Momami"},
"MKSKB250": {"arti": "Mmm Kids Shampoo-Kb250ml", "sku":  "V02502110177", "brand": "Momami"},
"MKKM5": {"arti": "Mmm Kind Kiddie Mask 5S", "sku":  "126780", "brand": "Momami"},
"MLBC500": {"arti": "Mmm Liquid Bottle Cleanser 500", "sku":  "126775", "brand": "Momami"},
"MLD900": {"arti": "Mmm Liquid Detergent 900Ml", "sku":  "126769", "brand": "Momami"},
"MLBC100": {"arti": "Mmm Lovely Baby Cologne 100Ml", "sku":  "131428", "brand": "Momami"},
"MMO100": {"arti": "Mmm Massage Oil 100Ml", "sku":  "126787", "brand": "Momami"},
"MNC15": {"arti": "Mmm Nipple Cream 15Gr", "sku":  "126786", "brand": "Momami"},
"MPBW": {"arti": "Mmm Pacifier & Bottle Wipes", "sku":  "121676", "brand": "Momami"},
"MPSAC": {"arti": "Mmm Pocket Sanitizer All Char", "sku":  "128482", "brand": "Momami"},
"MPSC": {"arti": "Mmm Pocket Sanitizer Cat", "sku":  "128481", "brand": "Momami"},
"MPSO": {"arti": "Mmm Pocket Sanitizer Octopus", "sku":  "128479", "brand": "Momami"},
"MPSW": {"arti": "Mmm Pocket Sanitizer Whale", "sku":  "128480", "brand": "Momami"},
"MRADSL50": {"arti": "Mmm Rub A Dub Sun Lotion 50Ml", "sku":  "128923", "brand": "Momami"},
"MSW": {"arti": "Mmm Saline Wipes", "sku":  "121678E", "brand": "Momami"},
"MSSS100": {"arti": "Mmm Shielding Sanitizer Spr100", "sku":  "126375", "brand": "Momami"},
"MSLT125": {"arti": "Mmm Silky Liquid Talc 125Ml", "sku":  "126617", "brand": "Momami"},
"MSLT70": {"arti": "Mmm Silky Liquid Talc 70Ml", "sku":  "V01302100034", "brand": "Momami"},
"MSTO100": {"arti": "Mmm Snuggly Telon Oil 100Ml", "sku":  "134848", "brand": "Momami"},
"MSTTT100": {"arti": "Mmm Softie Top To Toe 100Ml", "sku":  "V01302100032", "brand": "Momami"},
"MSTTT235": {"arti": "Mmm Softie Top To Toe 235Ml", "sku":  "126613", "brand": "Momami"},
"MSGAMC500": {"arti": "Mmm Spray Go-Away Mtsrf Cln500", "sku":  "126734", "brand": "Momami"},
"MSSGA60": {"arti": "Mmm Spray-Spray Go Away 60Ml", "sku":  "128917", "brand": "Momami"},
"MSC125": {"arti": "Mmm Stretchmark Cream 125Ml", "sku":  "126783", "brand": "Momami"},
"MSS50": {"arti": "Mmm Stretchmark Serum 50Gr", "sku":  "126784", "brand": "Momami"},
"MSBS100": {"arti": "Mmm Sunny Buddy Soothing 100Ml", "sku":  "128974", "brand": "Momami"},
"MSHS100": {"arti": "Mmm Sweet Hair Serum 100Ml", "sku":  "131427", "brand": "Momami"},
"MTGW20": {"arti": "Mmm Tooth & Gum 20", "sku":  "132870", "brand": "Momami"},
"MTGW30": {"arti": "Mmm Tooth & Gum Wipes 30S", "sku":  "136325", "brand": "Momami"},
"MTGW30P": {"arti": "Mmm Tooth&Gum Wipes 30S Peach", "sku":  "136796M", "brand": "Momami"},
"MTS20": {"arti": "Mmm Toothspray 20Ml", "sku":  "130151", "brand": "Momami"},
"MTSH20": {"arti": "Mmm Toothspray Honeydew 20Ml", "sku":  "133901", "brand": "Momami"},
"MTSP20": {"arti": "Mmm Toothspray Peach 20Ml", "sku":  "133899", "brand": "Momami"},
"MWW": {"arti": "Mmm Water Wipes", "sku":  "121677E", "brand": "Momami"},
"MWW3": {"arti": "Mmm Water Wipes 3Pk", "sku":  "136911M", "brand": "Momami"},
"MWW6": {"arti": "Mmm Water Wipes 6Pk", "sku":  "136912M", "brand": "Momami"},
"MZSBR": {"arti": "Mmm Zuper Sunnies Blue/Red", "sku":  "134064", "brand": "Momami"},
"MZSPD": {"arti": "Mmm Zuper Sunnies Pink/Darkpk", "sku":  "134066", "brand": "Momami"},
"MABL": {"arti": "Mmmxliunic Antibact Bl", "sku":  "132927", "brand": "Momami"},
"MXAPK": {"arti": "Mmmxliunic Antibact Pk", "sku":  "132926", "brand": "Momami"},
"MPSBL": {"arti": "Mmmxliunic Pocket Sanitizer Bl", "sku":  "132925", "brand": "Momami"},
"MXPSPK": {"arti": "Mmmxliunic Pocket Sanitizer Pk", "sku":  "132852", "brand": "Momami"},
"MBBY50": {"arti": "Momami Bouncy Baby Yogurt 50Ml", "sku":  "129289", "brand": "Momami"},
"MSLT50": {"arti": "Momami Silky Liquid Talc 50Ml", "sku":  "129290", "brand": "Momami"},
"MSTO100": {"arti": "MOMAMI Snuggly Telon Oil 100Ml", "sku":  "V02502110176", "brand": "Momami"},
"MSTTW": {"arti": "Momami Softie Top To Toe Wash", "sku":  "129288", "brand": "Momami"},
"MREK": {"arti": "Bdl Mmm Ramadhan Essential Kit", "sku":  "136802M", "brand": "Momami"},
"PBFMR": {"arti": "Peb Bundle Fisik Mom Range", "sku":  "V1003214647", "brand": "Pureats"},
"PFB": {"arti": "Peb Free Banpine", "sku":  "V0303216103", "brand": "Pureats"},
"PFD": {"arti": "Peb Free Dragmull", "sku":  "V0303216105", "brand": "Pureats"},
"PFDC": {"arti": "Peb Free Drkcho", "sku":  "V0303216104", "brand": "Pureats"},
"PFSM": {"arti": "Peb Free Strmgo", "sku":  "V0303216106", "brand": "Pureats"},
"PFDAPLMGO": {"arti": "Peb Freeze Dried Aplmgo 15G", "sku":  "132755", "brand": "Pureats"},
"PFDBNSTR": {"arti": "Peb Freeze Dried Banstr 15G", "sku":  "132705A", "brand": "Pureats"},
"PGCDC": {"arti": "Peb Granola Crunch Dark Choco", "sku":  "V0403202558", "brand": "Pureats"},
"PGCHB": {"arti": "Peb Granola Crunch Hny Berries", "sku":  "V0403202559", "brand": "Pureats"},
"PLT": {"arti": "Peb Pureats Lactation Tea", "sku":  "V25403202565", "brand": "Pureats"},
"PSBP": {"arti": "Peb Smoothie Melts Banpine 18G", "sku":  "132757", "brand": "Pureats"},
"PSMG": {"arti": "Peb Smoothie Melts Melgrape", "sku":  "132758A", "brand": "Pureats"},
"PSSTRM": {"arti": "Peb Smoothie Melts Strmgo 18G", "sku":  "132756", "brand": "Pureats"},
"PMMPB": {"arti": "Pureats  Melty Stick Mpb 30G", "sku":  "133115", "brand": "Pureats"},
"PMSTB": {"arti": "Pureats  Melty Stick Stb 30G", "sku":  "133114", "brand": "Pureats"},
"PAP": {"arti": "Pureats Apple Puffs 30G", "sku":  "133103", "brand": "Pureats"},
"PBRF": {"arti": "Pureats Bdl Ramadhan Fisik", "sku":  "V0303216102", "brand": "Pureats"},
"PBP": {"arti": "Pureats Berries Puffs 30G", "sku":  "133116", "brand": "Pureats"},
"PFDDM": {"arti": "Pureats Dried Fruit Dragmull", "sku":  "132705B", "brand": "Pureats"},
"PLB": {"arti": "Pureats Lactation Booster", "sku":  "V1003211967", "brand": "Pureats"},
"PMBO": {"arti": "Pureats Meltcrac Banana Oat", "sku":  "133060", "brand": "Pureats"},
"PMSP": {"arti": "Pureats Meltcrac Sweet Potato", "sku":  "133061", "brand": "Pureats"},
"PSP": {"arti": "Pureats Strawberry Puffs 30G", "sku":  "133059", "brand": "Pureats"},
"PVMP": {"arti": "Pureats Veggie Melts Pumpkin", "sku":  "132759B", "brand": "Pureats"},
"PVMS": {"arti": "Pureats Veggie Melts Spinach", "sku":  "132759A", "brand": "Pureats"},
"BMHBF": {"arti": "Bdl Mmm Hair & Body Foam", "sku":  "128894", "brand": "Pureats"},
"MKSMP250": {"arti": "Mmm Kids Shampoo-Mp250ml", "sku":  "V02502110176", "brand": "Momami"},
"MBOS": {"arti": "Mmm Buzz Off Spray", "sku":  "V02502110173", "brand": "Momami"},
"MCOOW": {"arti": "Mmm Cooling Wipes", "sku":  "136751M", "brand": "Momami"},
}

async def start(update, context):
    await update.message.reply_text(
        "Halo! Bot sudah aktif 🚀\n"
        "Ketik kode barang (misalnya MCSP-3 atau banyak item sekaligus), saya akan balas detailnya."
    )

async def lookup_code(update, context):
    text = update.message.text.strip().upper()
    lines = text.split("\n")   # pisahkan input per baris
    results = []

    for line in lines:
        if "-" in line:
            kode, qty = line.split("-", 1)
            kode = kode.strip().upper()
            qty = qty.strip()
        else:
            kode = line.strip().upper()
            qty = None

        detail = kode_dict.get(kode)
        if detail:
            arti = detail["arti"]
            sku = detail["sku"]
            brand = detail["brand"]

            reply_line = f"📦 {kode}\nNama: {arti}\nBrand: {brand}\nSKU: {sku}"
            if qty:
                reply_line += f"\nQty: {qty}"
            results.append(reply_line)
        else:
            results.append(f"Kode {kode} tidak ditemukan ❌")

    # gabungkan semua hasil jadi satu balasan
    reply = "\n\n".join(results)
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, lookup_code))
    app.run_polling()

if __name__ == "__main__":
    main()
