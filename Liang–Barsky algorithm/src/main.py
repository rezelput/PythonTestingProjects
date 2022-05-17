import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS

im = Image.new("RGB", (640,480))
im1 = Image.new("RGB", (640,480))
draw = ID.Draw(im)
draw2 = ID.Draw(im1)
draw.polygon((200, 200, 400 , 200,400,300,200,300), outline = 255)
draw2.polygon((200, 200, 400 , 200,400,300,200,300), outline = 255)
emax=(400.0,300.0)
emin=(200.0,200.0)
xmax=400.0;
ymax=300.0;
xmin=200.0;
ymin=200.0;
def ROUND(a):
	return (int(a+0.5));
def LiangBarsky(x1,y1,x2,y2):
	p = [0]*4;
	q = [0]*4;
	dx = x2 - x1;
	dy = y2 - y1;
	tmin = 0;
	tmax = 1;
	p[0] = -(x2 - x1);
	p[1] = (x2 - x1);
	p[2] = -(y2 - y1);
	p[3] = (y2 - y1);
	q[0] = x1 - xmin;
	q[1] = xmax - x1;
	q[2] = y1 - ymin;
	q[3] = ymax - y1;
	print(p);
	print(q);
	for i in range(0, 4):
		print(i);
		print("p = %f",p[i]);
		print("q = %f",q[i]);
		if(p[i] < 0):
			tmin = max(tmin, (q[i]/p[i]));
			print("tmin");
			print(tmin);
		elif(p[i] > 0):
			tmax = min(tmax, (q[i]/p[i]));
			print("tmax");
			print(tmax);
		elif(q[i] < 0):
				tmax = 0;
				tmin = 1;
				print("Comming Out of loop");
				break;
	if (tmin < tmax):
		print("(%i,%i)",ROUND(x1 + tmin * dx),ROUND(y1 + tmin * dx))
		draw.line(((x1 + tmin * dx), (y1 + tmin * dy), (x1 + tmax * dx), (y1 + tmax * dy)),fill=(255,255,255))
	else:
		print("Line lies outside");
def draw1(x1, y1, x2, y2):
    draw2.line((x1,y1,x2,y2),fill=(0,255,0))
    LiangBarsky(x1,y1,x2,y2)
draw1(300,250,375,250)    
draw1(150,250,300,350)
draw1(300,350,450,250)
draw1(450,250,300,150)
draw1(300,150,150,250)
draw1(150,325,450,175)
im.show();
im1.show()