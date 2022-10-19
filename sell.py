servicekey = 'K5fygs3Ao38zhEsyxA2qi4TnFk1O6Q4Rpwok1XdloMNXSfLFOf1VNbuUV7zKFSIZZvgnFw8Iz2cCqzO0Eyvoyw%3D%3D' #서비스키
numOfRows = '3'#기본 세팅
pageNo = '1'#기본 세팅
_returnType = 'json'#기본 세팅
examin_de = '20221018'#농수산물 도매가 날짜
prdlst_cd = '615'#농수산물 고유번호 (엑셀 참고)
url = 'https://apis.data.go.kr/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch?serviceKey=' + servicekey +'&numOfRows=' + numOfRows +'&pageNo=' + pageNo + '&_returnType=' + _returnType + '&examin_de=' + examin_de + '&prdlst_cd=' + prdlst_cd

print(url)