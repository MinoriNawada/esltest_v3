import random

from PIL import Image, ImageDraw, ImageFont
from barcode.writer import ImageWriter
import barcode

# 2.13inch - 200 * 122 px
# Design No.01
# DifferentColor ver.01
def make213_01_01(
        code=random.randrange(10**5, 10**6),
        jan=4973007525936,
        name="__name__ == __main__",
        price_ex=1,
        price_in=1,
        ):
    # フォントを指定
    f_name = ImageFont.truetype("YuGothB.ttc", 20) # 商品名
    f_price_ex = ImageFont.truetype("YuGothR.ttc", 12) # 税抜き価格
    f_price_in = ImageFont.truetype("YuGothB.ttc", 32) # 税込み価格
    f_code = ImageFont.truetype("YuGothR.ttc", 11) # 商品CD・JANCD
    f_yen = ImageFont.truetype("YuGothR.ttc", 12) # "円"

    # Barcodeの生成
    # Barcode(EAN13)を生成
    ean = barcode.get('EAN13', str(jan), writer=ImageWriter())
    # 生成したBacodeをImageとして保存
    # optionsでbarcodeのsizeを調整
    # そのために保存が必要
    # options指定時はファイル名に拡張子をつけない(理由は不明)
    # 一度保存しないとnewに合成できない
    ean.save("eslapp/static/images/barcode/ean_v1",options={
        'module_height': 4,
        'module_width': 0.5,
        'font_size': 0,
        'text_distance': 4
        })
    # barcodeImageをopen
    # barcodeImageの余白をcrop
    # barcodeImageを1modeに変換：Pmodeでは白部分がグレーになってしまうため1
    # barcodeImageを縮小
    ean_img = Image.open("eslapp/static/images/barcode/ean_v1.png")
    ean_img = ean_img.crop((50, 0, 650, 70))
    ean_img = ean_img.convert("1")
    ean_img = ean_img.resize((int(ean_img.width / 4), int(ean_img.height / 5)), Image.BOX)
    # barcodeのbaseImage="barcodeImg"を用意
    # newにBarcodeImageをpaste
    # barcodeImageにtextを書き込み
    # [error]newのカラーを(255, 255, 255)=白で指定するとバーコードが貼り付けられない、原因不明
    # [error]255のみで指定すると正しく表示されるので255指定で対処
    # [error](255, 255, 255)でもtextは問題なく表示される
    barcodeImg = Image.new("P", (150, 25), 255)
    barcodeImg.paste(ean_img, (0, 0))
    draw = ImageDraw.Draw(barcodeImg)
    draw.text((75, 22), f"{jan}", font=f_code, anchor="ms", fill=(0, 0, 0))

    # 商品名を表示する領域の生成
    # 黒(0, 0, 0)の画像を生成
    # img = Image.new("画像モード", (横, 縦), 色)
    img1 = Image.new("P", (250, 55), (0, 0, 0))
    # テキスト(255: white)を書き込み
    draw = ImageDraw.Draw(img1)
    draw.text((10, 5), f"{name}", font=f_name, fill=(255, 255, 255))

    # 詳細を表示する領域の生成
    # 白(255, 255, 255)の画像を生成
    img2 = Image.new("P", (250, 67), (255, 255, 255))
    # テキスト(0, 0, 0)を書き込み
    draw = ImageDraw.Draw(img2)
    draw.text((100, 34), f"税抜 {int(price_ex):,} 円", font=f_price_ex, anchor="rs", fill=(0, 0, 0))
    draw.text((220, 34), f"{int(price_in):,}", font=f_price_in, anchor="rs", fill=(0, 0, 0))
    draw.text((240, 34), "円", font=f_yen, anchor="rs", fill=(0, 0, 0))
    draw.text((240, 62), f"# {code}", font=f_code, anchor="rs", fill=0)

    # 2枚の画像ファイルを結合する
    # [error]結合のためのbaseはRGBモードにする
    # [error]Pmodeだとおかしな画像になる
    dst = Image.new('RGB', (img1.width, img1.height + img2.height), (255, 255, 255))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (0, img1.height))
    dst.paste(barcodeImg, (10, 40 + img1.height))
    
    # 画像を棚札に表示できる向きに回転
    dst = dst.transpose(Image.ROTATE_90)

    return dst


# DifferentColor ver.02
def make213_01_02(
        code=random.randrange(10**5, 10**6),
        jan=4973007525936,
        name="__name__ == __main__",
        price_ex=1,
        price_in=1,
        ):
    # フォントを指定
    f_name = ImageFont.truetype("YuGothB.ttc", 20) # 商品名
    f_price_ex = ImageFont.truetype("YuGothR.ttc", 12) # 税抜き価格
    f_price_in = ImageFont.truetype("YuGothB.ttc", 32) # 税込み価格
    f_code = ImageFont.truetype("YuGothR.ttc", 11) # 商品CD・JANCD
    f_yen = ImageFont.truetype("YuGothR.ttc", 12) # "円"

    # Barcodeの生成
    # Barcode(EAN13)を生成
    ean = barcode.get('EAN13', str(jan), writer=ImageWriter())
    # 生成したBacodeをImageとして保存
    # optionsでbarcodeのsizeを調整
    # そのために保存が必要
    # options指定時はファイル名に拡張子をつけない(理由は不明)
    # 一度保存しないとnewに合成できない
    ean.save("eslapp/static/images/barcode/ean_v1",options={
        'module_height': 4,
        'module_width': 0.5,
        'font_size': 0,
        'text_distance': 4
        })
    # barcodeImageをopen
    # barcodeImageの余白をcrop
    # barcodeImageを1modeに変換：Pmodeでは白部分がグレーになってしまうため1
    # barcodeImageを縮小
    ean_img = Image.open("eslapp/static/images/barcode/ean_v1.png")
    ean_img = ean_img.crop((50, 0, 650, 70))
    ean_img = ean_img.convert("1")
    ean_img = ean_img.resize((int(ean_img.width / 4), int(ean_img.height / 5)), Image.BOX)
    # barcodeのbaseImage="barcodeImg"を用意
    # newにBarcodeImageをpaste
    # barcodeImageにtextを書き込み
    # [error]newのカラーを(255, 255, 255)=白で指定するとバーコードが貼り付けられない、原因不明
    # [error]255のみで指定すると正しく表示されるので255指定で対処
    # [error](255, 255, 255)でもtextは問題なく表示される
    barcodeImg = Image.new("P", (150, 25), 255)
    barcodeImg.paste(ean_img, (0, 0))
    draw = ImageDraw.Draw(barcodeImg)
    draw.text((75, 22), f"{jan}", font=f_code, anchor="ms", fill=(0, 0, 0))

    # 商品名を表示する領域の生成
    # 赤(255, 0, 0)の画像を生成
    # img = Image.new("画像モード", (横, 縦), 色)
    img1 = Image.new("P", (250, 55), (255, 0, 0))
    # テキスト(255: white)を書き込み
    draw = ImageDraw.Draw(img1)
    draw.text((10, 5), f"{name}", font=f_name, fill=(255, 255, 255))

    # 詳細を表示する領域の生成
    # 白(255, 255, 255)の画像を生成
    img2 = Image.new("P", (250, 67), (255, 255, 255))
    # テキスト(0, 0, 0)を書き込み
    draw = ImageDraw.Draw(img2)
    draw.text((100, 34), f"税抜 {int(price_ex):,} 円", font=f_price_ex, anchor="rs", fill=(0, 0, 0))
    draw.text((220, 34), f"{int(price_in):,}", font=f_price_in, anchor="rs", fill=(0, 0, 0))
    draw.text((240, 34), "円", font=f_yen, anchor="rs", fill=(0, 0, 0))
    draw.text((240, 62), f"# {code}", font=f_code, anchor="rs", fill=0)

    # 2枚の画像ファイルを結合する
    # [error]結合のためのbaseはRGBモードにする
    # [error]Pmodeだとおかしな画像になる
    dst = Image.new('RGB', (img1.width, img1.height + img2.height), (255, 255, 255))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (0, img1.height))
    dst.paste(barcodeImg, (10, 40 + img1.height))
    
    # 画像を棚札に表示できる向きに回転
    dst = dst.transpose(Image.ROTATE_90)

    return dst


# DifferentColor ver.03
def make213_01_03(
        code=random.randrange(10**5, 10**6),
        jan=4973007525936,
        name="__name__ == __main__",
        price_ex=1,
        price_in=1,
        ):
    # フォントを指定
    f_name = ImageFont.truetype("YuGothB.ttc", 20) # 商品名
    f_price_ex = ImageFont.truetype("YuGothR.ttc", 12) # 税抜き価格
    f_price_in = ImageFont.truetype("YuGothB.ttc", 32) # 税込み価格
    f_code = ImageFont.truetype("YuGothR.ttc", 11) # 商品CD・JANCD
    f_yen = ImageFont.truetype("YuGothR.ttc", 12) # "円"

    # Barcodeの生成
    # Barcode(EAN13)を生成
    ean = barcode.get('EAN13', str(jan), writer=ImageWriter())
    # 生成したBacodeをImageとして保存
    # optionsでbarcodeのsizeを調整
    # そのために保存が必要
    # options指定時はファイル名に拡張子をつけない(理由は不明)
    # 一度保存しないとnewに合成できない
    ean.save("eslapp/static/images/barcode/ean_v1",options={
        'module_height': 4,
        'module_width': 0.5,
        'font_size': 0,
        'text_distance': 4
        })
    # barcodeImageをopen
    # barcodeImageの余白をcrop
    # barcodeImageを1modeに変換：Pmodeでは白部分がグレーになってしまうため1
    # barcodeImageを縮小
    ean_img = Image.open("eslapp/static/images/barcode/ean_v1.png")
    ean_img = ean_img.crop((50, 0, 650, 70))
    ean_img = ean_img.convert("1")
    ean_img = ean_img.resize((int(ean_img.width / 4), int(ean_img.height / 5)), Image.BOX)
    # barcodeのbaseImage="barcodeImg"を用意
    # newにBarcodeImageをpaste
    # barcodeImageにtextを書き込み
    # [error]newのカラーを(255, 255, 255)=白で指定するとバーコードが貼り付けられない、原因不明
    # [error]255のみで指定すると正しく表示されるので255指定で対処
    # [error](255, 255, 255)でもtextは問題なく表示される
    barcodeImg = Image.new("P", (150, 25), 255)
    barcodeImg.paste(ean_img, (0, 0))
    draw = ImageDraw.Draw(barcodeImg)
    draw.text((75, 22), f"{jan}", font=f_code, anchor="ms", fill=(0, 0, 0))

    # 商品名を表示する領域の生成
    # 黒(0, 0, 0)の画像を生成
    # img = Image.new("画像モード", (横, 縦), 色)
    img1 = Image.new("P", (250, 55), (0, 0, 0))
    # テキスト(255: white)を書き込み
    draw = ImageDraw.Draw(img1)
    draw.text((10, 5), f"{name}", font=f_name, fill=(255, 255, 255))

    # 詳細を表示する領域の生成
    # 白(255, 255, 255)の画像を生成
    img2 = Image.new("P", (250, 67), (255, 255, 255))
    # テキスト(0, 0, 0)を書き込み
    draw = ImageDraw.Draw(img2)
    draw.text((100, 34), f"税抜 {int(price_ex):,} 円", font=f_price_ex, anchor="rs", fill=(0, 0, 0))
    draw.text((220, 34), f"{int(price_in):,}", font=f_price_in, anchor="rs", fill=(255, 0, 0))
    draw.text((240, 34), "円", font=f_yen, anchor="rs", fill=(0, 0, 0))
    draw.text((240, 62), f"# {code}", font=f_code, anchor="rs", fill=0)

    # 2枚の画像ファイルを結合する
    # [error]結合のためのbaseはRGBモードにする
    # [error]Pmodeだとおかしな画像になる
    dst = Image.new('RGB', (img1.width, img1.height + img2.height), (255, 255, 255))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (0, img1.height))
    dst.paste(barcodeImg, (10, 40 + img1.height))
    
    # 画像を棚札に表示できる向きに回転
    dst = dst.transpose(Image.ROTATE_90)

    return dst



"""枠線をつける場合"""
# w, h = img2.size
# draw.rectangle((0, 0, w-1, h-1))

if __name__ == "__main__":
    make213_01_01()
    
