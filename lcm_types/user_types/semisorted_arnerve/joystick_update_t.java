/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package semisorted_arnerve;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class joystick_update_t implements lcm.lcm.LCMEncodable
{
    public String name;
    public byte numAxes;
    public int axes[];
    public byte numButtons;
    public byte buttons[];
    public byte numHats;
    public short hats[];
 
    public joystick_update_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0xf3749dd16a848cbdL;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(semisorted_arnerve.joystick_update_t.class))
            return 0L;
 
        classes.add(semisorted_arnerve.joystick_update_t.class);
        long hash = LCM_FINGERPRINT_BASE
            ;
        classes.remove(classes.size() - 1);
        return (hash<<1) + ((hash>>63)&1);
    }
 
    public void encode(DataOutput outs) throws IOException
    {
        outs.writeLong(LCM_FINGERPRINT);
        _encodeRecursive(outs);
    }
 
    public void _encodeRecursive(DataOutput outs) throws IOException
    {
        char[] __strbuf = null;
        __strbuf = new char[this.name.length()]; this.name.getChars(0, this.name.length(), __strbuf, 0); outs.writeInt(__strbuf.length+1); for (int _i = 0; _i < __strbuf.length; _i++) outs.write(__strbuf[_i]); outs.writeByte(0); 
 
        outs.writeByte(this.numAxes); 
 
        for (int a = 0; a < this.numAxes; a++) {
            outs.writeInt(this.axes[a]); 
        }
 
        outs.writeByte(this.numButtons); 
 
        if (this.numButtons > 0)
            outs.write(this.buttons, 0, numButtons);
 
        outs.writeByte(this.numHats); 
 
        for (int a = 0; a < this.numHats; a++) {
            outs.writeShort(this.hats[a]); 
        }
 
    }
 
    public joystick_update_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public joystick_update_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static semisorted_arnerve.joystick_update_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        semisorted_arnerve.joystick_update_t o = new semisorted_arnerve.joystick_update_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        char[] __strbuf = null;
        __strbuf = new char[ins.readInt()-1]; for (int _i = 0; _i < __strbuf.length; _i++) __strbuf[_i] = (char) (ins.readByte()&0xff); ins.readByte(); this.name = new String(__strbuf);
 
        this.numAxes = ins.readByte();
 
        this.axes = new int[(int) numAxes];
        for (int a = 0; a < this.numAxes; a++) {
            this.axes[a] = ins.readInt();
        }
 
        this.numButtons = ins.readByte();
 
        this.buttons = new byte[(int) numButtons];
        ins.readFully(this.buttons, 0, numButtons); 
        this.numHats = ins.readByte();
 
        this.hats = new short[(int) numHats];
        for (int a = 0; a < this.numHats; a++) {
            this.hats[a] = ins.readShort();
        }
 
    }
 
    public semisorted_arnerve.joystick_update_t copy()
    {
        semisorted_arnerve.joystick_update_t outobj = new semisorted_arnerve.joystick_update_t();
        outobj.name = this.name;
 
        outobj.numAxes = this.numAxes;
 
        outobj.axes = new int[(int) numAxes];
        if (this.numAxes > 0)
            System.arraycopy(this.axes, 0, outobj.axes, 0, this.numAxes); 
        outobj.numButtons = this.numButtons;
 
        outobj.buttons = new byte[(int) numButtons];
        if (this.numButtons > 0)
            System.arraycopy(this.buttons, 0, outobj.buttons, 0, this.numButtons); 
        outobj.numHats = this.numHats;
 
        outobj.hats = new short[(int) numHats];
        if (this.numHats > 0)
            System.arraycopy(this.hats, 0, outobj.hats, 0, this.numHats); 
        return outobj;
    }
 
}
