public class DemoTumpukan{
    public static void main(String[]args){
        Tumpukan t = new Tumpukan();

        Barang meja = new Barang ("Meja");
        Barang keyboard = new Barang ("keyboard");
        Barang Mouse = new barang ("mouse");

        t.tumpuk(meja);
        t.tumpuk(keyboard);
        t.tumpuk(mouse);

        t.lihatlahIsiTumpukan();

    
    }
}