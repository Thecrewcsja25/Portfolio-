from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON 1: Beiked: Las mejores galletas de Bogota
@app.get("/coordenadas/beiked")
def get_coordenadas_beiked():
    return [
        {
            "nombre": "Beiked C.C. Andino",
            "coords": [4.673176499332547, -74.05713970594813],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nqYxbHBv_a-ylEbZJWn1Ve6lObnUTzwQSBrwrN1PULVEwVGpqL2TXaNhfBLJH4I-gcgbbaIgm35jgcLnrSqIn98ZufMrvt742G37-sJRwMTN1Ytnr5Fvgwc1CVcM93zHVsjF5YS=w408-h544-k-no",
            "descripcion": "Un pedazo de felicidad en tus manos. Galletas tan suaves y perfectas que se deshacen en la boca. Hechas con amor y magia, listas para alegrar tu día",
            "ref": "o75Nd8ajIRE"
        },
        {
            "nombre": "Beiked Salitre Plaza",
            "coords": [4.659489109099787, -74.112414665653],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nr2Qe-QngRJQQ1w9XDMPdnTzSfGLVO2X_51lrvQocwK-2m5_e47g3LHPbLF7_SkrKSyclBZW1DeLSl7vqUns-jzMEa3biZXMJyVsdNb14NHViGCMPTW9rfnuQzbeRSGPmrxi5zx=w408-h544-k-no",
            "descripcion": "El aroma a galleta recién horneada te llama. En Beiked, cada galleta es una tentación irresistible. Un sabor que te transporta a casa y te hace desear más. ¡Cede al antojo!",
            "ref": "o75Nd8ajIRE"
        },
        {
            "nombre": "Beiked C.C. Santa Fe",
            "coords": [4.765921034163317, -74.04641670958442],
            "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSv2FPxatV1p0Mm9D9kULacyD_7VcoMj7wcGw&s",
            "descripcion": "Tu dosis de dulzura. Somos expertos en crear galletas que son más que un postre; son el momento de placer que te mereces. Ven y descubre tu nuevo sabor favorito",
            "ref": "o75Nd8ajIRE"
        }
    ]

# JSON 2: La Galiet: Reposteria
@app.get("/coordenadas/lagaliet")
def get_coordenadas_lagaliet():
    return [
        {
            "nombre": "La galiet PLaza Claro",
            "coords": [4.660867416990116, -74.10554786412226],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4npysq1g2ZjcXxCulouOWPurWRkAiqAf_zLZsJA5IJbsPTNoy_Vylp_AQk89tdCoGlKadjbI5CEP9fGbxHTYxlzrNY9Av0cwiijdsaIClw8j3SlHzFkMWP4HAHGO_KNNySDCO9Bg=w408-h510-k-no",
            "descripcion": "La Galiet: Creadores de felicidad. Somos los pioneros en galletas rellenas de Colombia desde 2017. Cada galleta es una experiencia única, hecha con amor y pasión para que descubras sabores que te harán sonreír (Cra. 68a #24b-10, Bogotá)",
            "ref": "ud_GAD14wd4"
        },
        {
            "nombre": "La galiet Chapinero",
            "coords": [4.660525229487483, -74.05610939084586],
            "imagen": "https://lh3.googleusercontent.com/p/AF1QipNsZ40ohAYEA1qVDhE29MEECDUUPyq9cbJ7dpYd=w408-h725-k-no",
            "descripcion": "Un bocado de arte y sabor. En La Galiet, fusionamos la repostería artesanal de inspiración europea con la riqueza de los sabores colombianos. Nuestra misión es simple: convertir un postre en un momento de pura felicidad (Cl. 71 # 5 - 23, Bogotá)",
            "ref": "ud_GAD14wd4"
        },
        {
            "nombre": "La galiet C.C. Titan Plaza",
            "coords": [4.703639538795479, -74.08632179118145],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4np2DUfiPYl2rU-anP6PM4Dak7glKu6wsjK__ZUeun5qpbeBPXqTDJ9W8CdhC4l8tNwEtB4h_o66y9w1Cdw6b2roYlDet_zWeuC30DtT-pRSgieQRIb8_pRKjDNQwl1Ooqmco621=w408-h307-k-no",
            "descripcion": "El lugar donde el antojo se hace realidad. Descubre nuestras galletas únicas, malteadas que te volarán la cabeza y bebidas para cada ocasión. La Galiet es tu escape perfecto para un dulce y merecido momento de placer (C.C. Tian PLaza)",
            "ref": "ud_GAD14wd4"
        },
        {
            "nombre": "La galiet La mariposa",
            "coords": [4.605773091523397, -74.0794553365597],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nqOgz9jZdWGNM_RBlFJmFL1jSwyWnF70IreUGcjdCIf4ScQK-I3Zf_N8I2Pn_SrFLgIPyhzfbt1IlTUH4N__miX1TUdrID9wyYIcke8hIluj3JTWNltqO76Ij13r-A4cWGQzvo9jg=w408-h545-k-no",
            "descripcion": "No son solo galletas, son pura magia. En La Galiet, cada galleta es diferente, con diferentes masas, rellenos y preparaciones. Ven y descubre por qué nuestra pasión por los postres nos hace únicos en Colombia (Cl. 12 #12-13, Bogotá)",
            "ref": "ud_GAD14wd4"
        },
        {
            "nombre": "La galiet Plaza de las Americas",
            "coords": [4.628701065155147, -74.13610358718894],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4npAg22HB-KqHfFqs_Ot6h5BOfrE1EosLaR_QGu2NJfCjqTsfHHDhEd3IQ0q_B6YMrBslcn3xN-LP__oiI_hzosutk5xvF4r2Ikz6PGuCbFOkxyYzcSxNIRMvDPqgAZCa3STuiyHxg=w408-h544-k-no",
            "descripcion": "La Galiet te lo pone fácil. ¿Antojo de algo dulce? Nuestro equipo de expertos panaderos ha preparado para ti las galletas rellenas más exquisitas de Bogotá. ¡No te quedes con las ganas! (Cra. 71d, Bogotá)",
            "ref": "ud_GAD14wd4"
        },
        {
            "nombre": "La galiet Cll. 140",
            "coords": [4.729301552431492, -74.04065986794697],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nroyFJfMODCkG-VZcrGV_Z7OMD2tBSKO07SUOFQksN4gknRGLPWlQxIgvWN985dyrugp0Sn7ZVtGajbkDpfJNcrwiDR8vJK7Y3ScmKinwQfobYcGfq3uRebFXykkwuNRRKLh9FT1A=w408-h544-k-no",
            "descripcion": "Más que galletas, un viaje de sabores. En La Galiet, cada receta es una historia. Descubre nuestras creaciones únicas, desde clásicos hasta sabores de temporada. ¡Elige tu aventura! (Cl. 140 #12B-90, Usaquén, Bogotá)",
            "ref": "ud_GAD14wd4"
        }
    ]

# JSON 3: Maiz Kernel
@app.get("/coordenadas/maiz-kernel")
def get_coordenadas_maiz_kernel():
    return [
        {
            "nombre": "Maiz-Kernel Cll. 185 ",
            "coords": [4.772366136407884, -74.0452691011067],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4npH2gHR8r8_37ctY2guhA80RJF2yts5DStJ7l9NwZDxfKmTFN6sSBz7-0KtfCuLEwx3vD_JUVAdzhGHZFPkT9_Rr9bQISGb29ryzj_170XmRqHX4_uVPTLl1ZTkopAwwM4DL85m3g=w408-h725-k-no",
            "descripcion": "Maíz Kernel: El crujido que lo cambia todo. Olvídate de los snacks aburridos. Aquí, cada grano es una explosión de sabor inesperado. ¡Dale una oportunidad a tu paladar y déjate sorprender! (C.C. Santa fe, Local 2-40, Bogotá)",
            "ref": "7X85xwlxHcM"
        },
        {
            "nombre": "Maiz-Kernel Cedritos",
            "coords": [4.735613185745861, -74.0486779553037],
            "imagen": "https://lh3.googleusercontent.com/p/AF1QipPPPlIjB-SEkqVJVjUQT9ncy5EE9M-NqSIDVXwF=w172-h224-p-k-no",
            "descripcion": "¡Bienvenido al núcleo del sabor! En Maíz Kernel, no hay límites para la creatividad. Transformamos el maíz en una obra de arte crujiente y llena de magia. ¿Listo para probar algo que te volará la cabeza? (Cra 19 #136a-06, Local 18b16, C.C. Sorpresas)",
            "ref": "7X85xwlxHcM"
        },
        {
            "nombre": "Maiz-Kernel Cll. 124",
            "coords": [4.718634090303459, -74.04085045547147],
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nrAhwY0hhPyQWeZLVcBWZ00hU7yeVVNIdDGQvS3NLcCAMbx4SqUX8HuVfJxLmD2uTTh759dAHH_s4a8RgMYdPTl1rvON-0duCdvVumGuJLMWacLwxd3BwtgcZNQi0Q203CQQonBJw=w408-h725-k-no",
            "descripcion": "La revolución del snhttpsack ha llegado. Esto no es solo un snack, es una experiencia que te hará decir: '¡WTF, esto es increíble!'. Maíz Kernel: el sabor que estabas buscando y que no sabías que necesitabas (Cra. 15 #124-30, Usaquén)",
            "ref": "7X85xwlxHcM"
        },
        {
            "nombre": "Maiz-Kernel Centro internacional",
            "coords": [4.633681366791113, -74.06836980620471],
            "imagen": "https://lh3.googleusercontent.com/p/AF1QipNcXbtCE-DCfBJzYRHLxm25ULCygUviHouOevet=w408-h544-k-no",
            "descripcion": "La magia está en el detalle. Cada grano es un viaje inesperado de sabor y textura. No es solo un snack, es el resultado de la obsesión por crear la experiencia más adictiva. ¡Pruébalos y no querrás parar! (Ak 7 #27-42, Centro de Bogotá)",
            "ref": "7X85xwlxHcM"
        },
        {
            "nombre": "Maiz-Kernel /plaza de las americas",
            "coords": [4.650412436725555, -74.13894918511679],
            "imagen": "https://lh3.googleusercontent.com/p/AF1QipN56q2T_qD44QGvSMLeHUKNqJDt5LSqWtb09lqS=w408-h544-k-no",
            "descripcion": "La magia está en el detalle. Cada grano es un viaje inesperado de sabor y textura. No es solo un snack, es el resultado de la obsesión por crear la experiencia más adictiva. ¡Pruébalos y no querrás parar! (Ak 7 #27-42, Centro de Bogotá)",
            "ref": "7X85xwlxHcM"
        }
    ]