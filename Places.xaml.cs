using System;
using System.Collections.Generic;
using System.Diagnostics;
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
    /// Логика взаимодействия для places.xaml
    /// </summary>
    public partial class places : Window
    {
        public places()
        {
            InitializeComponent();
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string urlxeno = "https://www.roblox.com/games/96190706334253/The-Building-Place-Objects-Update";

            try
            {
                // Для WPF в .NET (Core/5/6/7/8+) обязательно UseShellExecute = true
                Process.Start(new ProcessStartInfo
                {
                    FileName = urlxeno,
                    UseShellExecute = true
                });
            }

            catch (Exception) { }
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            // Открытие окна MainWindow.xaml
            MainWindow win2 = new MainWindow();
            win2.Show();
            this.Close();

        }

        private void RichTextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            string urlxeno = "https://www.roblox.com/games/106235470393240/BattleExperience";

            try
            {
                // Для WPF в .NET (Core/5/6/7/8+) обязательно UseShellExecute = true
                Process.Start(new ProcessStartInfo
                {
                    FileName = urlxeno,
                    UseShellExecute = true
                });
            }

            catch (Exception) { }
        }
    }
}
