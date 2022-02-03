﻿/*
 * Created by SharpDevelop.
 * User: mfern
 * Date: 2/2/2022
 * Time: 8:25 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Perceptron
{
	/// <summary>
	/// Description of window.
	/// </summary>
	public partial class Window : Form
	{
		Brush b = new SolidBrush(Color.Purple);
		Bitmap bmp;
		Graphics gf;
		public Window()
		{
			InitializeComponent();
		}
		void PictureBox1MouseClick(object sender, MouseEventArgs e)//escala de 30 centro 300,300
		{	
			MessageBox.Show(e.X.ToString()+", "+e.Y.ToString());
			
			int x=e.X/30;
			int y= e.Y/30;
			
			bmp = new Bitmap (pictureBox1.Width,pictureBox1.Height);
			gf= Graphics.FromImage(bmp);
			gf.Clear(Color.Transparent);
			gf.FillEllipse(b, new RectangleF(e.X,e.Y, 15, 15));
			
			pictureBox1.Image = bmp;
			pictureBox1.Refresh();
				
		}
		
		
		
		void PictureBox1Paint(object sender, PaintEventArgs e)
		{
			Pen pen_ = new Pen(Color.Black,2);
			
			SolidBrush sb = new SolidBrush(Color.Black);
			Font f = new Font("Times new roman", 12);
			int x_c=pictureBox1.Width/2;
			int y_c=pictureBox1.Height/2;
			double count=-1;
			double inc=0.10;
			e.Graphics.TranslateTransform(x_c,y_c);
			//e.Graphics.ScaleTransform(-1,1);
			
			e.Graphics.DrawLine(pen_,x_c*-1,0,x_c*2,0);
			e.Graphics.DrawLine(pen_,0,y_c,0,y_c*-1);
			
			for(int i=-x_c;i<x_c;i+=30){
				e.Graphics.DrawLine(pen_,5,i,-5,i);
				e.Graphics.DrawLine(pen_,i,5,i,-5);
				if(i!=0){
					
					e.Graphics.DrawString(""+(float)count,f,sb,i-8,5); //X
					e.Graphics.DrawString(""+(float)count*-1,f,sb,5,i-8);// Y
					
				}
				count=count+inc;
				
			}
		}


	}
}
