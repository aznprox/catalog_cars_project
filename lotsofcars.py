from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Make, Base, Model

engine = create_engine('sqlite:///carmake.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Acura Car Make

make1 = Make(name='Acura', image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Acura_logo.svg/1200px-Acura_logo.svg.png')

session.add(make1)
session.commit()

modelCar1 = Model(name='ILX', description='Meticulously-crafted with a stunning new A-Spec variant, this powerfully-styled premium sport sedan features an aggressive exterior re-design, along with a beautiful interior wrapped in Milano Leather and Ultrasuede trim. Inside and out, the ILX was tailor made for you.', price='$25,900',
                image='https://www.acura.com/-/media/Acura-Platform/Vehicle-Pages/ILX/2019/overview-page/Hero-and-Parallax/03-showroom/ILX_2019_Quick_On_Its_Feet_M.jpg', make=make1)

session.add(modelCar1)
session.commit()

modelCar2 = Model(name='TLX', description='With so many premium features, the 2020 Acura TLX is the best sport sedan for those who like to have it all.',
                price='33,000', image='https://www.acura.com/-/media/Acura-Platform/Vehicle-Pages/TLX/2020/overview-page-b/07-packages/2020_TLX_packages_A-Spec-Package_M.jpg', make=make1)

session.add(modelCar2)
session.commit()

modelCar3 = Model(name='RLX', description='Engineered to thrill in more ways than one, the 2019 RLX is performance personified. Available in 377-HP66 Sport Hybrid SH-AWD with 7-Speed DCT, or discover the 310-HP83 Precision All-Wheel Steer with 10-Speed Automatic Transmission.',
                price='$54,900', image='https://www.acura.com/-/media/Acura-Platform/Vehicle-Pages/RLX/2019/gallery-page/05-2019-acura-rlx-gallery-exterior-sport-hybrid-m.jpg', make=make1)

session.add(modelCar3)
session.commit()

modelCar4 = Model(name='RDX', description='The all new Acura RDX is redesigned, more luxurious, and even more thrilling to drive. Everything we ever imagined and then some.',
                price='$37,400', image='https://www.acura.com/-/media/Acura-Platform/Vehicle-Pages/RDX/2019/gallery-page/exterior/05-gallery-rdx-2019-aspec-white-diamond-pearl-showing-agressive-rear-led-taillights-M.jpg', make=make1)

session.add(modelCar4)
session.commit()

modelCar5 = Model(name='MDX', description='The 2019 Acura MDX is ready for the challenge. We designed the MDX around your lifestyle, no wonder it is the best-selling third-row luxury SUV of all time.',
                price='$44,300', image='https://www.acura.com/-/media/Acura-Platform/Vehicle-Pages/MDX/2019/overview-page/03_Gallery/02-gallery-MDX-2019-Advance-M.jpg', make=make1)

session.add(modelCar5)
session.commit()


print ("added makes and models!!!")