from app.api import bp
from flask import Blueprint, request, jsonify
@bp.route('/salo', methods=['GET'])
def getTabSalo():
    null = None
    res ={}
    res["status_code"] =200
    res["data"] ={
    "tribes": [
      {
        "tribe_id": 59,
        "name": "Abyssinian"
      },
      {
        "tribe_id": 331,
        "name": "Akita"
      },
      {
        "tribe_id": 216,
        "name": "Ald Xám Lông Ngắn Tai Cụp"
      },
      {
        "tribe_id": 49,
        "name": "Angora Thổ Nhĩ Kỳ"
      },
      {
        "tribe_id": 40,
        "name": "Anh Lông Dài"
      },
      {
        "tribe_id": 301,
        "name": "Anh Lông Dài Tai Cụp"
      },
      {
        "tribe_id": 39,
        "name": "Anh Lông Ngắn"
      },
      {
        "tribe_id": 242,
        "name": "Anh Lông Ngắn Lai Nga"
      },
      {
        "tribe_id": 172,
        "name": "Anh Lông Ngắn Lai Scottish"
      },
      {
        "tribe_id": 37,
        "name": "Ba Tư"
      },
      {
        "tribe_id": 199,
        "name": "Ba Tư Lai Anh Lông Dài"
      },
      {
        "tribe_id": 164,
        "name": "Ba Tư lai Anh Lông Ngắn"
      },
      {
        "tribe_id": 223,
        "name": "Ba Tư Lai Tai Cụp"
      },
      {
        "tribe_id": 289,
        "name": "Ba Tư Lai Thổ Nhĩ Kỳ"
      },
      {
        "tribe_id": 42,
        "name": "Bengal"
      },
      {
        "tribe_id": 248,
        "name": "Bombay"
      },
      {
        "tribe_id": 283,
        "name": "British Shorthair"
      },
      {
        "tribe_id": 157,
        "name": "Chartreux"
      },
      {
        "tribe_id": 69,
        "name": "Châu Âu Lông Ngắn"
      },
      {
        "tribe_id": 68,
        "name": "Chausie"
      },
      {
        "tribe_id": 67,
        "name": "Cộc Đuôi Nhật Bản"
      },
      {
        "tribe_id": 159,
        "name": "Con Lai Ngoại Quốc"
      },
      {
        "tribe_id": 51,
        "name": "Exotic"
      },
      {
        "tribe_id": 127,
        "name": "Feline"
      },
      {
        "tribe_id": 50,
        "name": "Himalaya"
      },
      {
        "tribe_id": 74,
        "name": "Hổ báo"
      },
      {
        "tribe_id": 66,
        "name": "Khao Manee"
      },
      {
        "tribe_id": 72,
        "name": "La Perm"
      },
      {
        "tribe_id": 151,
        "name": "Lai"
      },
      {
        "tribe_id": 220,
        "name": "Lai Nga"
      },
      {
        "tribe_id": 45,
        "name": "Maine Coon"
      },
      {
        "tribe_id": 71,
        "name": "Manx"
      },
      {
        "tribe_id": 64,
        "name": "Mau Ai Cập"
      },
      {
        "tribe_id": 144,
        "name": "Mèo ra"
      },
      {
        "tribe_id": 203,
        "name": "Mèo Ta"
      },
      {
        "tribe_id": 58,
        "name": "Miến Điện"
      },
      {
        "tribe_id": 70,
        "name": "Muffin"
      },
      {
        "tribe_id": 165,
        "name": "Munchkin"
      },
      {
        "tribe_id": 161,
        "name": "Munchkin Anh Lông Ngắn"
      },
      {
        "tribe_id": 43,
        "name": "Munhkin"
      },
      {
        "tribe_id": 167,
        "name": "Mướp"
      },
      {
        "tribe_id": 46,
        "name": "Mỹ Lông Ngắn"
      },
      {
        "tribe_id": 55,
        "name": "Mỹ Tai Xoắn"
      },
      {
        "tribe_id": 229,
        "name": "Nga Lông Dài"
      },
      {
        "tribe_id": 48,
        "name": "Nga xanh"
      },
      {
        "tribe_id": 251,
        "name": "Nuốt Dưa Hấu"
      },
      {
        "tribe_id": 62,
        "name": "Oriental Lông Ngắn"
      },
      {
        "tribe_id": 47,
        "name": "Ragdoll"
      },
      {
        "tribe_id": 60,
        "name": "Rừng"
      },
      {
        "tribe_id": 61,
        "name": "Rừng Nauy"
      },
      {
        "tribe_id": 226,
        "name": "Samsut"
      },
      {
        "tribe_id": 273,
        "name": "Săn Bắt Côn Trùng"
      },
      {
        "tribe_id": 52,
        "name": "Savannah"
      },
      {
        "tribe_id": 173,
        "name": "Scottish"
      },
      {
        "tribe_id": 174,
        "name": "Scottish Fold"
      },
      {
        "tribe_id": 275,
        "name": "Scottish Lai Anh Lông Dài"
      },
      {
        "tribe_id": 274,
        "name": "Scottish Thuần Lai Ald Trắng"
      },
      {
        "tribe_id": 239,
        "name": "Siberian"
      },
      {
        "tribe_id": 56,
        "name": "Somali"
      },
      {
        "tribe_id": 214,
        "name": "Sphynx"
      },
      {
        "tribe_id": 44,
        "name": "Sphynx - Ai Cập"
      },
      {
        "tribe_id": 103,
        "name": "Ta"
      },
      {
        "tribe_id": 218,
        "name": "Ta (Mướp)"
      },
      {
        "tribe_id": 215,
        "name": "Ta (Tam Thể)"
      },
      {
        "tribe_id": 252,
        "name": "Ta (Trắng)"
      },
      {
        "tribe_id": 253,
        "name": "Ta (Vàng)"
      },
      {
        "tribe_id": 321,
        "name": "Ta Lai"
      },
      {
        "tribe_id": 145,
        "name": "Ta Lai Anh Lông Dài"
      },
      {
        "tribe_id": 180,
        "name": "Ta Lai Anh Lông Ngắn"
      },
      {
        "tribe_id": 171,
        "name": "Ta Lai Lông Ngắn"
      },
      {
        "tribe_id": 299,
        "name": "Ta Xăm Trổ, Rất Nguy Hiểm"
      },
      {
        "tribe_id": 244,
        "name": "Tabby Lông Ngắn"
      },
      {
        "tribe_id": 245,
        "name": "Tabi Việt Nam Thuần Chủng"
      },
      {
        "tribe_id": 38,
        "name": "Tai Cụp"
      },
      {
        "tribe_id": 156,
        "name": "Tam Thể"
      },
      {
        "tribe_id": 53,
        "name": "Thái"
      },
      {
        "tribe_id": 65,
        "name": "Thần Miến Điện"
      },
      {
        "tribe_id": 63,
        "name": "Tonkinese"
      },
      {
        "tribe_id": 54,
        "name": "Toyger"
      },
      {
        "tribe_id": 247,
        "name": "Trắng"
      },
      {
        "tribe_id": 57,
        "name": "Turkish Van"
      },
      {
        "tribe_id": 246,
        "name": "Vàng"
      },
      {
        "tribe_id": 41,
        "name": "Xiêm"
      }
    ],
    "provinces": [
      {
        "province_id": 1000,
        "name": "Toàn quốc"
      },
      {
        "province_id": 1,
        "name": "Hà Nội"
      },
      {
        "province_id": 79,
        "name": "Hồ Chí Minh"
      },
      {
        "province_id": 89,
        "name": "An Giang"
      },
      {
        "province_id": 77,
        "name": "Bà Rịa - Vũng Tàu"
      },
      {
        "province_id": 24,
        "name": "Bắc Giang"
      },
      {
        "province_id": 6,
        "name": "Bắc Kạn"
      },
      {
        "province_id": 95,
        "name": "Bạc Liêu"
      },
      {
        "province_id": 27,
        "name": "Bắc Ninh"
      },
      {
        "province_id": 83,
        "name": "Bến Tre"
      },
      {
        "province_id": 74,
        "name": "Bình Dương"
      },
      {
        "province_id": 52,
        "name": "Bình Định"
      },
      {
        "province_id": 70,
        "name": "Bình Phước"
      },
      {
        "province_id": 60,
        "name": "Bình Thuận"
      },
      {
        "province_id": 96,
        "name": "Cà Mau"
      },
      {
        "province_id": 92,
        "name": "Cần Thơ"
      },
      {
        "province_id": 4,
        "name": "Cao Bằng"
      },
      {
        "province_id": 48,
        "name": "Đà Nẵng"
      },
      {
        "province_id": 66,
        "name": "Đắk Lắk"
      },
      {
        "province_id": 67,
        "name": "Đắk Nông"
      },
      {
        "province_id": 11,
        "name": "Điện Biên"
      },
      {
        "province_id": 75,
        "name": "Đồng Nai"
      },
      {
        "province_id": 87,
        "name": "Đồng Tháp"
      },
      {
        "province_id": 64,
        "name": "Gia Lai"
      },
      {
        "province_id": 2,
        "name": "Hà Giang"
      },
      {
        "province_id": 35,
        "name": "Hà Nam"
      },
      {
        "province_id": 42,
        "name": "Hà Tĩnh"
      },
      {
        "province_id": 30,
        "name": "Hải Dương"
      },
      {
        "province_id": 31,
        "name": "Hải Phòng"
      },
      {
        "province_id": 93,
        "name": "Hậu Giang"
      },
      {
        "province_id": 17,
        "name": "Hòa Bình"
      },
      {
        "province_id": 33,
        "name": "Hưng Yên"
      },
      {
        "province_id": 56,
        "name": "Khánh Hòa"
      },
      {
        "province_id": 91,
        "name": "Kiên Giang"
      },
      {
        "province_id": 62,
        "name": "Kon Tum"
      },
      {
        "province_id": 12,
        "name": "Lai Châu"
      },
      {
        "province_id": 68,
        "name": "Lâm Đồng"
      },
      {
        "province_id": 20,
        "name": "Lạng Sơn"
      },
      {
        "province_id": 10,
        "name": "Lào Cai"
      },
      {
        "province_id": 80,
        "name": "Long An"
      },
      {
        "province_id": 36,
        "name": "Nam Định"
      },
      {
        "province_id": 40,
        "name": "Nghệ An"
      },
      {
        "province_id": 37,
        "name": "Ninh Bình"
      },
      {
        "province_id": 58,
        "name": "Ninh Thuận"
      },
      {
        "province_id": 25,
        "name": "Phú Thọ"
      },
      {
        "province_id": 54,
        "name": "Phú Yên"
      },
      {
        "province_id": 44,
        "name": "Quảng Bình"
      },
      {
        "province_id": 49,
        "name": "Quảng Nam"
      },
      {
        "province_id": 51,
        "name": "Quảng Ngãi"
      },
      {
        "province_id": 22,
        "name": "Quảng Ninh"
      },
      {
        "province_id": 45,
        "name": "Quảng Trị"
      },
      {
        "province_id": 94,
        "name": "Sóc Trăng"
      },
      {
        "province_id": 14,
        "name": "Sơn La"
      },
      {
        "province_id": 72,
        "name": "Tây Ninh"
      },
      {
        "province_id": 34,
        "name": "Thái Bình"
      },
      {
        "province_id": 19,
        "name": "Thái Nguyên"
      },
      {
        "province_id": 38,
        "name": "Thanh Hóa"
      },
      {
        "province_id": 46,
        "name": "Thừa Thiên Huế"
      },
      {
        "province_id": 82,
        "name": "Tiền Giang"
      },
      {
        "province_id": 84,
        "name": "Trà Vinh"
      },
      {
        "province_id": 8,
        "name": "Tuyên Quang"
      },
      {
        "province_id": 86,
        "name": "Vĩnh Long"
      },
      {
        "province_id": 26,
        "name": "Vĩnh Phúc"
      },
      {
        "province_id": 15,
        "name": "Yên Bái"
      }
    ],
    "genders": [
      {
        "name": "Đực",
        "gender": "male"
      },
      {
        "name": "Cái",
        "gender": "female"
      },
      {
        "name": "LGBT",
        "gender": "lgbt"
      }
    ],
    "sex_prices": [
      {
        "lable": "0 - 500K",
        "value": 1,
        "range": {
          "gte": 0,
          "lt": 500000
        }
      },
      {
        "lable": "500K - 1TR",
        "value": 2,
        "range": {
          "gte": 500000,
          "lt": 1000000
        }
      },
      {
        "lable": "1TR - 2TR",
        "value": 3,
        "range": {
          "gte": 1000000,
          "lt": 2000000
        }
      },
      {
        "lable": "2TR - 3TR",
        "value": 4,
        "range": {
          "gte": 2000000,
          "lt": 3000000
        }
      },
      {
        "lable": "3TR - 5TR",
        "value": 5,
        "range": {
          "gte": 3000000,
          "lt": 5000000
        }
      },
      {
        "lable": "5TR - 10TR",
        "value": 6,
        "range": {
          "gte": 5000000,
          "lt": 10000000
        }
      },
      {
        "lable": "> 10TR",
        "value": 7,
        "range": {
          "gte": 10000000
        }
      }
    ]
  }
    return jsonify(res)