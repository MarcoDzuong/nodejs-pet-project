from flask import Blueprint, request, jsonify
home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/home', methods=['GET'])
def getTabHome():
    null = None
    res ={}
    res["status_code"] =200
    res["data"] ={
    "my_boss": [
      {
        "id": 1601,
        "name": "huh",
        "avatar": "storage\/pets\/avatar_630988567_37-6efb-4a51.png",
        "birthday": "01\/08\/2021",
        "gender": "male",
        "species": "Chó Alaska",
        "age": "1 tháng 4 ngày"
      },
      {
        "id": 1602,
        "name": "higuh",
        "avatar": "storage\/pets\/avatar_651816932_eb-2de5-4fae.png",
        "birthday": "17\/06\/2021",
        "gender": "male",
        "species": "Mèo Angora Thổ Nhĩ Kỳ",
        "age": "2 tháng 18 ngày"
      },
      {
        "id": 1603,
        "name": "djdj",
        "avatar": "storage\/pets\/avatar_667702029_a2-3d79-4e1a.png",
        "birthday": "14\/07\/2021",
        "gender": "male",
        "species": "Chim Angora Thổ Nhĩ Kỳ",
        "age": "1 tháng 22 ngày"
      },
      {
        "id": 1604,
        "name": "uêu",
        "avatar": "storage\/pets\/avatar_672709660_01-a790-4e31.png",
        "birthday": "14\/07\/2021",
        "gender": "female",
        "species": "Chim Anh Lông Dài",
        "age": "1 tháng 22 ngày"
      },
      {
        "id": 1605,
        "name": "test",
        "avatar": "storage\/pets\/avatar_667961511_0e-2f45-42ff.png",
        "birthday": "03\/08\/2021",
        "gender": "female",
        "species": "Chó Alaska",
        "age": "1 tháng 2 ngày"
      }
    ],
    "events": [
      {
        "id": 13674,
        "title": "Tẩy giun lần2",
        "facility": null,
        "address": null,
        "date": "24\/09\/2021",
        "hour": "10:00",
        "status": 1,
        "boss_id": 1605,
        "boss_name": "test",
        "boss_avatar": "storage\/pets\/avatar_667961511_0e-2f45-42ff.png",
        "boss_gender": "female",
        "note": null,
        "type": 4,
        "age": ""
      },
      {
        "id": 13330,
        "title": "Vacxin FIP lần1",
        "facility": null,
        "address": null,
        "date": "17\/10\/2021",
        "hour": "10:00",
        "status": 1,
        "boss_id": 1602,
        "boss_name": "higuh",
        "boss_avatar": "storage\/pets\/avatar_651816932_eb-2de5-4fae.png",
        "boss_gender": "male",
        "note": null,
        "type": 4,
        "age": ""
      },
      {
        "id": 13331,
        "title": "Vacxin phòng dại lần1",
        "facility": null,
        "address": null,
        "date": "17\/10\/2021",
        "hour": "10:00",
        "status": 1,
        "boss_id": 1602,
        "boss_name": "higuh",
        "boss_avatar": "storage\/pets\/avatar_651816932_eb-2de5-4fae.png",
        "boss_gender": "male",
        "note": null,
        "type": 4,
        "age": ""
      },
      {
        "id": 13319,
        "title": "Vacxin phòng dại lần1",
        "facility": null,
        "address": null,
        "date": "01\/11\/2021",
        "hour": "10:00",
        "status": 1,
        "boss_id": 1601,
        "boss_name": "huh",
        "boss_avatar": "storage\/pets\/avatar_630988567_37-6efb-4a51.png",
        "boss_gender": "male",
        "note": null,
        "type": 4,
        "age": ""
      },
      {
        "id": 13342,
        "title": "Vacxin phòng dại lần1",
        "facility": null,
        "address": null,
        "date": "03\/11\/2021",
        "hour": "10:00",
        "status": 1,
        "boss_id": 1605,
        "boss_name": "test",
        "boss_avatar": "storage\/pets\/avatar_667961511_0e-2f45-42ff.png",
        "boss_gender": "female",
        "note": null,
        "type": 4,
        "age": ""
      }
    ],
    "banners": [
      {
        "id": 3,
        "title": "Chia sẻ ngay với bạn bè ứng dụng Petory nhận ngay quà siêu hấp dẫn",
        "order": 1,
        "type": 1,
        "status": 1,
        "description": "<p><strong><img src=\"storage\/banners\/description\/banner_cf-bcf3-4044.png\" alt=\"\" width=\"375\" height=\"200\" \/><\/strong><\/p>\r\n<p><strong>Lorem Ipsum is simply dummy text of the printing and typesetting industry.<\/strong><\/p>\r\n<p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.<\/p>\r\n<p>Đi c&ugrave;ng với chương tr&igrave;nh thăm kh&aacute;m miễn ph&iacute; l&agrave; qu&agrave; tặng sức khỏe hữu &iacute;ch từ Jio Health d&agrave;nh cho những kh&aacute;ch h&agrave;ng tham gia Doctor Tour. Qu&agrave; tặng gồm:<\/p>",
        "url": null,
        "image": "storage\/banners\/banner_a8-1966-47ee.png",
        "updated_at": "2021-07-29 23:36:11"
      },
      {
        "id": 4,
        "title": "Chia sẻ ngay với bạn bè ứng dụng Petory nhận ngay quà siêu hấp dẫn",
        "order": 2,
        "type": 2,
        "status": 1,
        "description": null,
        "url": "https:\/\/cancuocthucung.vn\/",
        "image": "storage\/banners\/banner_0c-84e2-4dee.png",
        "updated_at": "2021-07-29 23:36:53"
      }
    ]
    }
    return jsonify(res)