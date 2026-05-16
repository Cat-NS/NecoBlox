using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Diagnostics;
using System.IO.Enumeration;

namespace NecoBlox
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }


        private void Button_Click(object sender, RoutedEventArgs e)
        {
        
            Process.Start("files/rbxplayer.exe");
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            string urlxeno = "https://xeno.now/download";

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

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            Process.Start("files/closerbx.cmd");
        }

        private void Button_Click_3(object sender, RoutedEventArgs e)
        {
            Process.Start("files/studio.exe");
        }

        private void Button_Click_4(object sender, RoutedEventArgs e)
        {
            Process.Start("files/closestudio.cmd");
        }

        private void Button_Click_5(object sender, RoutedEventArgs e)
        {
            places win2 = new places();

            // 2. Показываем его
            win2.Show();

            // 3. Закрываем текущее (в котором нажата кнопка)
            this.Close();
        }

        private void Button_Click_6(object sender, RoutedEventArgs e)
        {
            userplaces winsss = new userplaces();
            winsss.Show();
            this.Close();
        }
    }
}