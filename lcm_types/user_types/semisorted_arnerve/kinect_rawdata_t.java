/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package semisorted_arnerve;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class kinect_rawdata_t implements lcm.lcm.LCMEncodable
{
    public int NUMIMAGEBYTES;
    public byte imagejpg_rgb[];
    public byte imagejpg_depth[];
    public int NUMJOINTS;
    public semisorted_arnerve.kinect_joint_t bodyjoints[];
 
    public kinect_rawdata_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x83f3c2f97d2f262dL;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(semisorted_arnerve.kinect_rawdata_t.class))
            return 0L;
 
        classes.add(semisorted_arnerve.kinect_rawdata_t.class);
        long hash = LCM_FINGERPRINT_BASE
             + semisorted_arnerve.kinect_joint_t._hashRecursive(classes)
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
        outs.writeInt(this.NUMIMAGEBYTES); 
 
        if (this.NUMIMAGEBYTES > 0)
            outs.write(this.imagejpg_rgb, 0, NUMIMAGEBYTES);
 
        if (this.NUMIMAGEBYTES > 0)
            outs.write(this.imagejpg_depth, 0, NUMIMAGEBYTES);
 
        outs.writeInt(this.NUMJOINTS); 
 
        for (int a = 0; a < this.NUMJOINTS; a++) {
            this.bodyjoints[a]._encodeRecursive(outs); 
        }
 
    }
 
    public kinect_rawdata_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public kinect_rawdata_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static semisorted_arnerve.kinect_rawdata_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        semisorted_arnerve.kinect_rawdata_t o = new semisorted_arnerve.kinect_rawdata_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.NUMIMAGEBYTES = ins.readInt();
 
        this.imagejpg_rgb = new byte[(int) NUMIMAGEBYTES];
        ins.readFully(this.imagejpg_rgb, 0, NUMIMAGEBYTES); 
        this.imagejpg_depth = new byte[(int) NUMIMAGEBYTES];
        ins.readFully(this.imagejpg_depth, 0, NUMIMAGEBYTES); 
        this.NUMJOINTS = ins.readInt();
 
        this.bodyjoints = new semisorted_arnerve.kinect_joint_t[(int) NUMJOINTS];
        for (int a = 0; a < this.NUMJOINTS; a++) {
            this.bodyjoints[a] = semisorted_arnerve.kinect_joint_t._decodeRecursiveFactory(ins);
        }
 
    }
 
    public semisorted_arnerve.kinect_rawdata_t copy()
    {
        semisorted_arnerve.kinect_rawdata_t outobj = new semisorted_arnerve.kinect_rawdata_t();
        outobj.NUMIMAGEBYTES = this.NUMIMAGEBYTES;
 
        outobj.imagejpg_rgb = new byte[(int) NUMIMAGEBYTES];
        if (this.NUMIMAGEBYTES > 0)
            System.arraycopy(this.imagejpg_rgb, 0, outobj.imagejpg_rgb, 0, this.NUMIMAGEBYTES); 
        outobj.imagejpg_depth = new byte[(int) NUMIMAGEBYTES];
        if (this.NUMIMAGEBYTES > 0)
            System.arraycopy(this.imagejpg_depth, 0, outobj.imagejpg_depth, 0, this.NUMIMAGEBYTES); 
        outobj.NUMJOINTS = this.NUMJOINTS;
 
        outobj.bodyjoints = new semisorted_arnerve.kinect_joint_t[(int) NUMJOINTS];
        for (int a = 0; a < this.NUMJOINTS; a++) {
            outobj.bodyjoints[a] = this.bodyjoints[a].copy();
        }
 
        return outobj;
    }
 
}

