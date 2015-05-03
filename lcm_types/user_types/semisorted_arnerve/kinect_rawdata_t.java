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
    public int NUMRGBBYTES;
    public int NUMDEPTHBYTES;
    public byte imagejpg_rgb[];
    public byte imagejpg_depth[];
    public semisorted_arnerve.kinect_joint_t bodyjoints[];
 
    public kinect_rawdata_t()
    {
        bodyjoints = new semisorted_arnerve.kinect_joint_t[25];
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x8f7e696b264ff6e7L;
 
    public static final byte SpineBase = (byte) 0;
    public static final byte SpineMid = (byte) 1;
    public static final byte Neck = (byte) 2;
    public static final byte Head = (byte) 3;
    public static final byte ShoulderLeft = (byte) 4;
    public static final byte ElbowLeft = (byte) 5;
    public static final byte WristLeft = (byte) 6;
    public static final byte HandLeft = (byte) 7;
    public static final byte ShoulderRight = (byte) 8;
    public static final byte ElbowRight = (byte) 9;
    public static final byte WristRight = (byte) 10;
    public static final byte HandRight = (byte) 11;
    public static final byte HipLeft = (byte) 12;
    public static final byte KneeLeft = (byte) 13;
    public static final byte AnkleLeft = (byte) 14;
    public static final byte FootLeft = (byte) 15;
    public static final byte HipRight = (byte) 16;
    public static final byte KneeRight = (byte) 17;
    public static final byte AnkleRight = (byte) 18;
    public static final byte FootRight = (byte) 19;
    public static final byte SpineShoulder = (byte) 20;
    public static final byte HandTipLeft = (byte) 21;
    public static final byte ThumbLeft = (byte) 22;
    public static final byte HandTipRight = (byte) 23;
    public static final byte ThumbRight = (byte) 24;

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
        outs.writeInt(this.NUMRGBBYTES); 
 
        outs.writeInt(this.NUMDEPTHBYTES); 
 
        if (this.NUMRGBBYTES > 0)
            outs.write(this.imagejpg_rgb, 0, NUMRGBBYTES);
 
        if (this.NUMDEPTHBYTES > 0)
            outs.write(this.imagejpg_depth, 0, NUMDEPTHBYTES);
 
        for (int a = 0; a < 25; a++) {
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
        this.NUMRGBBYTES = ins.readInt();
 
        this.NUMDEPTHBYTES = ins.readInt();
 
        this.imagejpg_rgb = new byte[(int) NUMRGBBYTES];
        ins.readFully(this.imagejpg_rgb, 0, NUMRGBBYTES); 
        this.imagejpg_depth = new byte[(int) NUMDEPTHBYTES];
        ins.readFully(this.imagejpg_depth, 0, NUMDEPTHBYTES); 
        this.bodyjoints = new semisorted_arnerve.kinect_joint_t[(int) 25];
        for (int a = 0; a < 25; a++) {
            this.bodyjoints[a] = semisorted_arnerve.kinect_joint_t._decodeRecursiveFactory(ins);
        }
 
    }
 
    public semisorted_arnerve.kinect_rawdata_t copy()
    {
        semisorted_arnerve.kinect_rawdata_t outobj = new semisorted_arnerve.kinect_rawdata_t();
        outobj.NUMRGBBYTES = this.NUMRGBBYTES;
 
        outobj.NUMDEPTHBYTES = this.NUMDEPTHBYTES;
 
        outobj.imagejpg_rgb = new byte[(int) NUMRGBBYTES];
        if (this.NUMRGBBYTES > 0)
            System.arraycopy(this.imagejpg_rgb, 0, outobj.imagejpg_rgb, 0, this.NUMRGBBYTES); 
        outobj.imagejpg_depth = new byte[(int) NUMDEPTHBYTES];
        if (this.NUMDEPTHBYTES > 0)
            System.arraycopy(this.imagejpg_depth, 0, outobj.imagejpg_depth, 0, this.NUMDEPTHBYTES); 
        outobj.bodyjoints = new semisorted_arnerve.kinect_joint_t[(int) 25];
        for (int a = 0; a < 25; a++) {
            outobj.bodyjoints[a] = this.bodyjoints[a].copy();
        }
 
        return outobj;
    }
 
}

