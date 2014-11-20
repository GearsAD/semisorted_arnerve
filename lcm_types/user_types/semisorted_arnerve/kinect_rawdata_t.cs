/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

using System;
using System.Collections.Generic;
using System.IO;
using LCM.LCM;
 
namespace semisorted_arnerve
{
    public sealed class kinect_rawdata_t : LCM.LCM.LCMEncodable
    {
        public int NUMIMAGEBYTES;
        public byte[] imagejpg_rgb;
        public byte[] imagejpg_depth;
        public int NUMJOINTS;
        public semisorted_arnerve.kinect_joint_t[] bodyjoints;
 
        public kinect_rawdata_t()
        {
        }
 
        public static readonly ulong LCM_FINGERPRINT;
        public static readonly ulong LCM_FINGERPRINT_BASE = 0x15a044367fd34a52L;
 
        static kinect_rawdata_t()
        {
            LCM_FINGERPRINT = _hashRecursive(new List<String>());
        }
 
        public static ulong _hashRecursive(List<String> classes)
        {
            if (classes.Contains("semisorted_arnerve.kinect_rawdata_t"))
                return 0L;
 
            classes.Add("semisorted_arnerve.kinect_rawdata_t");
            ulong hash = LCM_FINGERPRINT_BASE
                 + semisorted_arnerve.kinect_joint_t._hashRecursive(classes)
                ;
            classes.RemoveAt(classes.Count - 1);
            return (hash<<1) + ((hash>>63)&1);
        }
 
        public void Encode(LCMDataOutputStream outs)
        {
            outs.Write((long) LCM_FINGERPRINT);
            _encodeRecursive(outs);
        }
 
        public void _encodeRecursive(LCMDataOutputStream outs)
        {
            outs.Write(this.NUMIMAGEBYTES); 
 
            for (int a = 0; a < this.NUMIMAGEBYTES; a++) {
                outs.Write(this.imagejpg_rgb[a]); 
            }
 
            for (int a = 0; a < this.NUMIMAGEBYTES; a++) {
                outs.Write(this.imagejpg_depth[a]); 
            }
 
            outs.Write(this.NUMJOINTS); 
 
            for (int a = 0; a < this.NUMJOINTS; a++) {
                this.bodyjoints[a]._encodeRecursive(outs); 
            }
 
        }
 
        public kinect_rawdata_t(byte[] data) : this(new LCMDataInputStream(data))
        {
        }
 
        public kinect_rawdata_t(LCMDataInputStream ins)
        {
            if ((ulong) ins.ReadInt64() != LCM_FINGERPRINT)
                throw new System.IO.IOException("LCM Decode error: bad fingerprint");
 
            _decodeRecursive(ins);
        }
 
        public static semisorted_arnerve.kinect_rawdata_t _decodeRecursiveFactory(LCMDataInputStream ins)
        {
            semisorted_arnerve.kinect_rawdata_t o = new semisorted_arnerve.kinect_rawdata_t();
            o._decodeRecursive(ins);
            return o;
        }
 
        public void _decodeRecursive(LCMDataInputStream ins)
        {
            this.NUMIMAGEBYTES = ins.ReadInt32();
 
            this.imagejpg_rgb = new byte[(int) NUMIMAGEBYTES];
            for (int a = 0; a < this.NUMIMAGEBYTES; a++) {
                this.imagejpg_rgb[a] = ins.ReadByte();
            }
 
            this.imagejpg_depth = new byte[(int) NUMIMAGEBYTES];
            for (int a = 0; a < this.NUMIMAGEBYTES; a++) {
                this.imagejpg_depth[a] = ins.ReadByte();
            }
 
            this.NUMJOINTS = ins.ReadInt32();
 
            this.bodyjoints = new semisorted_arnerve.kinect_joint_t[(int) NUMJOINTS];
            for (int a = 0; a < this.NUMJOINTS; a++) {
                this.bodyjoints[a] = semisorted_arnerve.kinect_joint_t._decodeRecursiveFactory(ins);
            }
 
        }
 
        public semisorted_arnerve.kinect_rawdata_t Copy()
        {
            semisorted_arnerve.kinect_rawdata_t outobj = new semisorted_arnerve.kinect_rawdata_t();
            outobj.NUMIMAGEBYTES = this.NUMIMAGEBYTES;
 
            outobj.imagejpg_rgb = new byte[(int) NUMIMAGEBYTES];
            for (int a = 0; a < this.NUMIMAGEBYTES; a++) {
                outobj.imagejpg_rgb[a] = this.imagejpg_rgb[a];
            }
 
            outobj.imagejpg_depth = new byte[(int) NUMIMAGEBYTES];
            for (int a = 0; a < this.NUMIMAGEBYTES; a++) {
                outobj.imagejpg_depth[a] = this.imagejpg_depth[a];
            }
 
            outobj.NUMJOINTS = this.NUMJOINTS;
 
            outobj.bodyjoints = new semisorted_arnerve.kinect_joint_t[(int) NUMJOINTS];
            for (int a = 0; a < this.NUMJOINTS; a++) {
                outobj.bodyjoints[a] = this.bodyjoints[a].Copy();
            }
 
            return outobj;
        }
    }
}

