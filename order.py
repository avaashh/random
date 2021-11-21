import requests

cookies = {
    'XSRF-TOKEN': 'f4b93fe0-35ec-492e-9070-1777c2abe64a',
    '_aid': 'eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiZGlyIn0..7PL3OFVnm_F0S-S9.MB-4G0A_5AuD9U9nW81eU9VdMGaS-PATLSbJBq7iiFgc0DblhWTz-IUOA6KwKAkDZhP0yhNMCyYF18Uon5_f32uz6FBpQMGH_1RG-nsAr21h2MGHb4n2D6T7KCNpOC5VvHWfJN2ZXchR6OKE0wb-ku73GJT_QjXsLzLvnk8MFJsiayHiaqVqCP31xLEY2nvNxKXmwU37AagdbWwhQQcMia9FXmOyqOTYsTgwkNa3OI4dmKWFaLMP6SadbW0VFyhlGBoCoYuoAToHivP7NCukWYrBwkbw9-jwAP74WxwceWqEvGrzmHxBSvl2jI6PYhS5ow0iGPEFoObY-C1q0bCf_GkWVxJunE0dADG-IIB2fRPNhd9N1egZmbosfbsh6WOi_at0IfrGPdh-7QsSGcJoR8NYgOLcjW6M7vaS-67WcP0VHaLhTnh5CC-O34PxecCJVYlwxrFD_FUo0VpimpniBZ4usCwA_BJTnsK9VjHWtZMbPn3SJosWk4lk4bIRO8sy0RviNlVlQHvtalI-OWxlXdNQMV83kHJMcWwTXjac5SF03JekxDBtXQdNGJkvDeRGfVhqqETNZB5DJFsrgA.iBxps6o238T8JebjrYg_AA',
    '_rid': 'eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiZGlyIn0..6iRKkrRFLelHMODk.sBLuxERwiz_zVFFa3PCW-wiwnEutSoLSSpjSg6ctvmZ3IRH49gIhy3IICH8pGFwlMjrayVWPE0ay0NBcy1wNUTxM6Fjv-JgZO4aPyEmAaRKUeLlp8hR98frtrt296p6W3cMzCj2MU1TSpEgu6Zw4_zFGCuJROdcV9yET6RHGNPb6L83jj6ox3-RCIAmd1E-PpV8i_lG_yAI-OEjs6BpBsWc1hH7hw5JYAsOQhlUYt1H5Eqyj9xIZCjgbrwlAxF9HqX6pPqIpV2bs9Gbc1dxJ-HRNOACDb14zTILHzOZWAr5ecr43-hYCpHZVJy8y_B5JmtqqQd87pwSM-3ErUf5ymujJZ2AZf0MYQUbn5csEkxwnwnRg_w_DFdBbhbW0OJ423RIlu4K-RX49AJGhukAeygnq61LFlKAeTFiep1s_nIORwTgJAIaAB379sE4gSQlI515Y2hqEzkacyDtbyiuD2AbE3wb0-CUZ21wAv7PRiAFP4pM4yDt9HK1XUTwySdoVc97mmrhhvp-fh1NX1te3QCHiMG2hqD1MxI8b-wiH8ggijACmAd_YVPWd-q4nJbauhLr9jeqrHHgYGtO1QA.cERqy-1eHL6CLZT5ojEMVw',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'X-XSRF-TOKEN': 'f4b93fe0-35ec-492e-9070-1777c2abe64a',
    'Request-Owner': '100499',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Host-Session-Id': 'TWpRPS1hYjhiZTMyNy0xZjY1LTQ3ZTUtOGY3Yy01YzBhOGM1ZGFlZDA=',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://tms47.nepsetms.com.np',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://tms47.nepsetms.com.np/tms/me/memberclientorderentry',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = '{"orderBook":{"orderBookExtensions":[{"orderTypes":{"id":1,"orderTypeCode":"LMT"},"disclosedQuantity":0,"orderValidity":{"id":1,"orderValidityCode":"DAY"},"triggerPrice":0,"orderPrice":374,"orderQuantity":250,"remainingOrderQuantity":250,"marketType":{"id":2,"marketType":"Continuous"}}],"exchange":{"id":1},"dnaConnection":{},"dealer":{},"member":{},"productType":{"id":1,"productCode":"CNC"},"instrumentType":{"id":1,"code":"EQ"},"client":{"activeStatus":"A","id":2161094,"accountType":"CLI","allowedToTrade":"Y","clientMemberCode":"20210601253","clientOrDealer":"C","contactNumber":null,"emailId":null,"notsUniqueClientCode":"202106142324629","clientDealerType":null,"clientGroup":{"activeStatus":"A","id":101,"clientGroupCode":null,"clientGroupName":null},"memberBranch":{"activeStatus":"A","id":1,"branchLocation":null,"branchName":null,"hidden":null,"branchProvince":null,"branchDistrict":null,"branchMunicipality":null,"branchHead":null,"branchPhoneNumber":null},"clientDealerAddressDetails":null,"clientDealerBankDetail":null,"clientDealerIndividual":null,"clientDealerPerTradeLimits":null,"clientDealerProductMappings":null,"clientDealerOrderTypeMappings":null,"clientDealerTradingLimits":null,"clientDepositoryDetail":null,"corporateDetail":null,"corporateOwnershipDetails":null,"displayName":"Avaash Bhattarai","blockedDate":null,"remarks":null,"parentId":null,"recordType":null,"collateralByEntities":null,"shortSellMode":0,"onlineOrOffline":1,"panNumber":null,"onlineFundTransfer":null,"collateralCalculationMode":1,"isMarginLendingClient":null,"clientRiskType":null,"userAgreementChecked":null,"referredBy":null,"marginLendingClient":null},"security":{"id":136,"exchangeSecurityId":136,"marketProtectionPercentage":0,"divisor":100,"boardLotQuantity":1,"tickSize":0.1},"accountType":1,"cpMemberId":0,"buyOrSell":2},"orderPlacedBy":2,"exchangeOrderId":null}'

response = requests.post('https://tms47.nepsetms.com.np/tmsapi/orderApi/orderbook-v2/', headers=headers, cookies=cookies, data=data)
