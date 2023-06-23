import paho.mqtt.publish as publish
import datetime
import base64


def mqttESLGateway_run(productCode, deviceCode, deviceMac):
    # IP AddressはAWSのインスタンスを起動するたびに変わるので都度変更する
    broker = "18.182.43.46"

    ###################################################
    #  Yalatec Gateway用のformat                      #
    ###################################################

    # "Queue of data transmission and updating"の時は以下のtopic名にする
    topicName = "test/refresh/queue"

    # The unique identification number of the data sending
    # queue. This field is used for correspondence when
    # submitting the data sending result. After the same price
    # tag is successfully processed, the queue will cache the
    # latest queue identification number. After the same price
    # tag is successfully sent, continue to send the same
    # queue. By identifying the identification number, it will
    # directly return to success without any download and
    # screen refreshing actions.
    # 任意の値でよいが、結果が正しく反映されたかどうかを確認する際には
    # この値をキーとして確認するので一意の値にしておく。
    # ここではyymmddhmmttをセットすることとした。
    dt = datetime.datetime.now()
    queueid = int(dt.strftime("%Y%m%d%H%M%S"))

    # Equipment type. The default is 1 and others are invalid.
    deviceType = 1

    # device ID. The appearance of the electronic price tag is
    # marked with a unique number, which serves as an
    # identification for the user's visible operation.
    deviceCode = f'{deviceCode}'

    # Device MAC with 16-bit HEX encoding. The unique code
    # of the electronic price tag hardware is used as the
    # communication identifier between the base station and
    # the price base. How to get price tag MAC:
    # - The price tag system can be inquired by coding.
    # - The device code MAC correspondence table attached
    #   at the time of shipment.
    # - Restore the factory interface to view by resetting the
    #   price tag.
    deviceMac = f'{deviceMac}'

    # The software version of the price tag device. The base
    # station performs corresponding processing before
    # forwarding data according to the different version of the
    # price tag software. The server can store the software
    # version information for each price tag as needed, and
    # deliver it every time it is issued. If the server does not
    # record the information, it can be fixedly transmitted
    # according to the sample value.
    deviceVersion = '4.3.F'

    # Refresh action. in:
    # - 0x01: download data.
    # - 0x02: refresh the screen.
    # x01 is used to download pictures to the designated
    # storage area;
    # 0x02 is used to display pictures in the designated storage
    # area;
    # At the same time, set it to refresh immediately after
    # downloading the picture.
    # つまり 3 をセットするとダウンロードとリフレッシュが同時におこなわれる
    refreshAction = 3

    # Picture storage area. Just fix it to 1. If you need to use
    # other storage areas, please make sure that the price tag
    # hardware and firmware support this function.
    refreshArea = 1

    # Refresh the content array.
    # This item can be omitted when the content to be
    # displayed has been downloaded to the internal storage
    # area of the price tag in advance.

    #ファイルを読み込んでエンコードし、直接Gatewayに送信する
    # src_file = 'ESLImage005.bmp'
    src_file = f"D:\\django\\esltest_v3\\eslapp\\static\\images\\{productCode}.png"
    
    f = open(src_file, 'br')
    bin = f.read()
    b64data = base64.b64encode(bin)

    varMsg = '{'  +\
            '"queueId": ' + str(queueid) + ', '  +\
            '"deviceType": ' + str(deviceType) + ', ' +\
            '"deviceCode": "' + deviceCode + '", '  +\
            '"deviceMac": "' + deviceMac + '", ' +\
            '"deviceVersion": "' + deviceVersion + '", '  +\
            '"refreshAction": '  + str(refreshAction) + ', '  +\
            '"refreshArea": ' + str(refreshArea) + ', ' +\
            '"content": [{'  +\
                '"dataType": 3,'  +\
                '"dataRef": "' + b64data.decode("utf-8") + '"'  +\
            '}]'  +\
            '}'
            
    #テスト出力
    print(varMsg)

    # データ送信
    publish.single(topicName,varMsg,hostname=broker)

if __name__ == "__main__":
    mqttESLGateway_run()