/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package semisorted_arnerve;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class kinect_joint_t implements lcm.lcm.LCMEncodable
{
    public double position[];
    public double orientation[];
    public byte istracking;
 
    public kinect_joint_t()
    {
        position = new double[3];
        orientation = new double[4];
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x197734cf05d46d9eL;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(semisorted_arnerve.kinect_joint_t.class))
            return 0L;
 
        classes.add(semisorted_arnerve.kinect_joint_t.class);
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
        for (int a = 0; a < 3; a++) {
            outs.writeDouble(this.position[a]); 
        }
 
        for (int a = 0; a < 4; a++) {
            outs.writeDouble(this.orientation[a]); 
        }
 
        outs.writeByte(this.istracking); 
 
    }
 
    public kinect_joint_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public kinect_joint_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static semisorted_arnerve.kinect_joint_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        semisorted_arnerve.kinect_joint_t o = new semisorted_arnerve.kinect_joint_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.position = new double[(int) 3];
        for (int a = 0; a < 3; a++) {
            this.position[a] = ins.readDouble();
        }
 
        this.orientation = new double[(int) 4];
        for (int a = 0; a < 4; a++) {
            this.orientation[a] = ins.readDouble();
        }
 
        this.istracking = ins.readByte();
 
    }
 
    public semisorted_arnerve.kinect_joint_t copy()
    {
        semisorted_arnerve.kinect_joint_t outobj = new semisorted_arnerve.kinect_joint_t();
        outobj.position = new double[(int) 3];
        System.arraycopy(this.position, 0, outobj.position, 0, 3); 
        outobj.orientation = new double[(int) 4];
        System.arraycopy(this.orientation, 0, outobj.orientation, 0, 4); 
        outobj.istracking = this.istracking;
 
        return outobj;
    }
 
}

