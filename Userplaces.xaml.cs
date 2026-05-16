using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace NecoBlox
{
    /// <summary>
    /// Логика взаимодействия для userplaces.xaml
    /// </summary>
    public partial class userplaces : Window
    {
        public userplaces()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Discord: necostudiosofficial. (Send to discord place link and desctription, your place be added or not added in next update)");
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            MainWindow windoss = new MainWindow();
            windoss.Show();
            this.Close();
        }
    }
}
