import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class App extends JFrame {
    public static void main(String[] args) throws Exception {
        App f = new App();
        JPanel panel = new JPanel();
        // Right Here
        JLabel label = new JLabel("My first GUI");
        JButton button = new JButton("Clicky");

        panel.add(label);
        panel.add(button);

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int result = 2 + 2;
                JOptionPane.showMessageDialog(null, "2+2=" + result);
            }
        });
        f.setTitle("My Empty Frame");
        f.setSize(300, 200); // default size is 0,0
        f.setLocation(10, 200); // default is 0,0 (top left corner)
        f.getContentPane().add(panel);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}